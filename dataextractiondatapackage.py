import json
import glob, os, string
from openpyxl import Workbook, load_workbook
import pygeoj
import collections
import datetime
from time import strftime

path=os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

FirmLicenseWorkbookfile = glob.glob("../Firm Licenses.xlsx")[0]
FirmLicenseWorkbook = load_workbook(FirmLicenseWorkbookfile)
FirmLicenseSheet = FirmLicenseWorkbook["Sheet1"]
data = FirmLicenseSheet['A:H']
StateInitials = FirmLicenseSheet['B'][1:]

inmemorydata = [];listtuple = []
for state in FirmLicenseSheet.rows:
    listtuple = []
    for j in state:
        listtuple.append(j.value)
    inmemorydata.append(listtuple)

        
	

		
states_url = 'M:/Grow People/Licenses/ZZZ-Scripts for Map/states20m.json'

states = pygeoj.load(filepath=states_url)
attributes = states.all_attributes

outfile = pygeoj.new()
outfile.define_crs(type="link", link="http://spatialreference.org/ref/epsg/4326/esriwkt/", link_type="esriwkt")

for state in states:
    geometry = state.geometry
    for item in state.properties.iteritems():
        if item[0] == u'NAME':
            StateName = item[1]
        if item[0] == u'STUSPS':
            StateInitials = item[1]
            for FirmLicenseState in inmemorydata:
                if FirmLicenseState[1] == StateInitials:
                    try:
                        to = strftime('%m/%d/%Y',FirmLicenseState[4])
                        tr = strftime('%m/%d/%Y',FirmLicenseState[5])
                    except TypeError:
                        to = ""
                        tr = ""
                    outfile.add_feature(properties={"State":StateName,"License #":FirmLicenseState[3],
                    "Original Issue Date":to,"Renewal":tr,"Completed By":FirmLicenseState[6],
                    "Notes":FirmLicenseState[7]},geometry = geometry)

outfile.add_all_bboxes()
outfile.update_bbox()
outfile.add_unique_id()
outfile.save("joinedData.geojson")

        
