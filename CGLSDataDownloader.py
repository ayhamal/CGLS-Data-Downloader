# Package Dependencies:
# conda install rpy2
# conda install -c r r-rcurl
# conda install -c r r-codetools
# conda install -c conda-forge r-ncdf4
# conda install -c conda-forge r-raster

import os
import rpy2.robjects as robjects

# Import r object
r = robjects.r

# Register R source scripts
r['source']('Copernicus-Global-Land-Service-Data-Download-with-R/land.CopernicusDataDownload.R')

# Importing R functions as Python functions
downloadCGLSData = robjects.globalenv['download.CGLS.data']
ncOpenCGLSData = robjects.globalenv['nc_open.CGLS.data']
ncvarGetCGSLData = robjects.globalenv['ncvar_get_CGSL.data']
stackCGLSData = robjects.globalenv['stack.CGLS.data']

# - Description of Variables:
#
# downloadsPath : TARGET DIRECTORY, default: ./Downloads
# userName : USERNAME
# password : PASSWORD
# timeFrame : TIMEFRAME OF INTEREST, for example June 2019
# product : PRODUCT VARIABLE; CHOSE FROM fapar, fcover, lai, ndvi, ssm, swi, lst...
# resolution : RESOLTION; CHOSE FROM  1km, 300m or 100m
# version : VERSION; CHOSE FROM "v1", "v2", "v3"...

downloadsPath = os.getcwd()+'\\Downloads'
userName = 'Yttrium'
password = 'Guillermo123'
timeFrame = '2021-04-05'
specificDate = '2021-04-05'
product = 'swi'
resolution = '1km'
version = 'v1'
variable = ''

if not os.path.exists(downloadsPath):
    os.makedirs(downloadsPath)

downloadCGLSData(downloadsPath, userName, password, timeFrame, product, resolution, version)
ncOpenCGLSData(downloadsPath, specificDate, product, resolution, version)
ncvarGetCGSLData(downloadsPath, specificDate, product, resolution, version, variable)
stackCGLSData(downloadsPath, timeFrame, product, resolution, version, variable)
