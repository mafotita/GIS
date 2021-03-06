#!/usr/bin/env/ python

### Script to reapply geographic coordinates from preprossed to postprocessed TIF images.
### This script requires GDAL to run. ArcPy is not used due to licensing issues.

from osgeo import gdal,ogr,osr
import os
#from __future__ import print_function
gdal.UseExceptions()

  #The projCheck function will iterate through input directory and make sure files are in correct proection.
  #This should be run on both pre and post processed images to double-check integrity.
  #I'm pretty sure the GetProjection function is the incorrect one to use but it's pretty much a
  #placeholder for now.

def projCheck(r):
  if not r.GetProjection is WGS84:
    print "file %s is not in WGS84 projection. Cannot continue." %r
    sys.exit(1)
  elif r.GetProe is None and geotransform is None:
    print "No projection found in %s" %r
    sys.exit(1)


### This should take an input file and check whether or not it already is assigned a projection. If coordinates
### are not found, then coordinates of a matching filename are applied.

def applyRefs(input):
  print "processing %s" %input
  in_file = gdal.open(input)
  gt = in_file.GetGeoTransform()

  if geotransform is not None:
    x, x_size, x_rot, y, y_rot, y_size = geotransform
    world_file.write('%s\n' % x_size)
    world_file.write('%s\n' % x_rot)
    world_file.write('%s\n' % y_rot)
    world_file.write('%s\n' % y_size)
    world_file.write('%s\n' % x)
    world_file.write('%s\n' % y)
    world_file.close()

    ''' geotransform tuple key:
    [0] /* top left x */
    [1] /* w-e pixel resolution */
    [2] /* rotation, 0 if image is "north up" */
    [3] /* top left y */
    [4] /* rotation, 0 if image is "north up" */
    [5] /* n-s pixel resolution */
    '''
  else:
    print "sucks to be you."

tifs = []

def srchFl(dir):
  if not os.path.exists(dir):
    print "directory %s does not exist. Exiting" %dir
    sys.exit()
  else:
    for file in os.listdir(dir):
      if file.endswith(".tif"):
        tifs.extend(file)

preDir = raw_input("Please enter the directory in which the pre-processed GTIF files reside: ")
postDir = raw_input("Please enter the directory in which the post-processed GTIF files reside: ")
outDir = raw_input("Please enter the directory in which the final, fixed GTIF files should be placed: ")
raw_input("GeoTifs should be projected in WGS84. Press Enter to check projection of input files.")

for r in preDir:
  projCheck

for r in postDir:
  projCheck

