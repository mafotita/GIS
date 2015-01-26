#!/usr/bin/env/ python

### Script to reapply geographic coordinates from preprossed to postprocessed TIF images.
### This script requires GDAL to run. ArcPy is not used due to licensing issues.

import gdal
import os

def projCheck(r):
  #This function will iterate through input directory and make sure files are in correct proection.
  #This should be run on both pre and post processed images to double-check integrity.
  if not r.GetProjection is WGS84:
    print "file %s is not in WGS84 projection. Cannot continue." %r
    sys.exit()

def applyRefs(input, output):
  print "processing %s" %input
  in_file = gdal.open(input)
  gt = in_file.GetGeoTransform()
  if not geotransform is None:
    print 'Origin = (',geotransform[0], ',',geotransform[3],')'
  else:
    print" this is where the function to copy world file info to processed tif will go"

preDir = raw_input("Please enter the directory in which the pre-processed GTIF files reside: ")
postDir = raw_input("Please enter the directory in which the post-processed GTIF files reside: ")
raw_input("GeoTifs should be projected in WGS84. Press Enter to check projection of input files.")

for r in preDir:
  projCheck

for r in postDir:
  projCheck

