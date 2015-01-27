#!/usr/bin/env/ python

### Script to reapply geographic coordinates from preprossed to postprocessed TIF images.
### This script requires GDAL to run. ArcPy is not used due to licensing issues.

from osgeo import gdal,ogr,osr
import os
gdal.UseExceptions()

  """
  The projCheck function will iterate through input directory and make sure files are in correct proection.
  This should be run on both pre and post processed images to double-check integrity.
  I'm pretty sure the GetProjection function is the incorrect one to use but it's pretty much a
  placeholder for now.
  """
def projCheck(r):
  if not r.GetProjection is WGS84:
    print "file %s is not in WGS84 projection. Cannot continue." %r
    sys.exit()
### This should take an input file and check whether or not it already is assigned a projection. If coordinates
### are not found, then coordinates of a matching filename are applied.

def applyRefs(input, outDir):
  print "processing %s" %input
  in_file = gdal.open(input)
  gt = in_file.GetGeoTransform()
  if not geotransform is None:
    print 'Origin = (',geotransform[0], ',',geotransform[3],')'
  else:
    print" this is where the function to copy world file info to processed tif will go"

preDir = raw_input("Please enter the directory in which the pre-processed GTIF files reside: ")
postDir = raw_input("Please enter the directory in which the post-processed GTIF files reside: ")
outDir = raw_input("Please enter the directory in which the final, fixed GTIF files should be placed: ")
raw_input("GeoTifs should be projected in WGS84. Press Enter to check projection of input files.")

for r in preDir:
  projCheck

for r in postDir:
  projCheck

