# excelJoinToGeoJSON
Join Excel to GeoJSON Files

Step 1: create Anaconda environment with same packages as Arcmap 10.5

Workflow borrowed largely from following site:
https://gis.stackexchange.com/questions/119503/getting-arcpy-to-work-with-anaconda

For ArcMap 10.5 run the following code from the anaconda 32 bit command prompt which came with the install. Using this command prompt means the path variables do not need to be changed to run everything. Be sure to open prompt with administrative priviledges.

Conda create -n arc105 python=2.7.12
Conda activate arc105 #This will mean that you will install packages only in this environment, not messing up the root environment.

Conda install numpy=1.9.3

Note: matplotlib needs to be installed from pip using version 1.5.2, just like arcmap 10.5
pip install -Iv https://pypi.python.org/packages/1d/ad/8b00320ca3846fa3fede4f8f998844cef7a9d19511bd7596b85ae1493070/matplotlib-1.5.2-cp27-cp27m-win32.whl#md5=bf4722dd25c02bd5fc0db9f9fcb032e2

or for Arcmap 10.3.1 - follow previous steps

Conda create -n arc1031 python=2.7.8 #proceed when advised, should install dependencies for python as well.
activate arc1031

Before installing numpy, the original numpy may need to be uninstalled. Continue through all dialogues

conda remove numpy
conda install numpy=1.7.1

the packages present in this environment can be found by entering the following code:
Conda list

now install matplot lib, except version 1.3.0. This version is on the conda repository

conda install matplotlib=1.3.0

Now we need to let arcgis find anaconda and anaconda find arcgis. This is accomplished through .pth files placed in the site-packages directory as shown below.



