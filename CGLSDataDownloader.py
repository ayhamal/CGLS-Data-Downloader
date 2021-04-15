# Package Dependencies:
# conda install rpy2
# conda install -c r r-rcurl
# conda install -c r r-codetools
# conda install -c conda-forge r-ncdf4
# conda install -c conda-forge r-raster

import rpy2.robjects as robjects

r = robjects.r

r['source']('Copernicus-Global-Land-Service-Data-Download-with-R/land.CopernicusDataDownload.R')
r['source']('Copernicus-Global-Land-Service-Data-Download-with-R/HelloWorld.R')

# function(path, username, password, timeframe, product, resolution, version)
downloadCGLSData = robjects.globalenv['download.CGLS.data']
# function(path, date, product, resolution, version)
ncOpenCGLSData = robjects.globalenv['nc_open.CGLS.data']
# function(path, date, product, resolution, version, variable)
ncvarGetCGSLData = robjects.globalenv['ncvar_get_CGSL.data']
# function(path, timeframe, product, resolution, version, variable)
stackCGLSData = robjects.globalenv['stack.CGLS.data']

downloadCGLSData('E:\Projects\Python\CGLS Data Downloader\Downloads', 'Yttrium', 'Guillermo123', '2021-04-05', 'swi', "1km", "v1")
ncOpenCGLSData('E:\Projects\Python\CGLS Data Downloader\Downloads', '2021-04-05', 'swi', '1km', 'v1')
# ncvarGetCGSLData(path, date, product, resolution, version, variable)
# stackCGLSData(path, timeframe, product, resolution, version, variable)

r_getname = robjects.globalenv['SayHello']

r_getname()

print("ok")
