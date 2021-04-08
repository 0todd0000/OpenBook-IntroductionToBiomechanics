
'''
Utility script for resizing images to a specified width
'''

import os,glob,unipath
from math import floor
from PIL import Image



# get paths to all images
dir_root = unipath.Path( os.path.dirname(__file__) ).parent.parent
dir0     = os.path.join(dir_root, 'Tutorials', 'src', '02-InstallBlender')
fnames   = glob.glob( os.path.join(dir0, 'img', '*.png' ) )


# resize all images
w1       = 1000   # new image width
for fname in fnames:
	print(fname)
	img   = Image.open(fname)
	w0,h0 = img.size
	if w0 > w1:
		h1    = floor(w1 * h0/w0)
		img   = img.resize( (w1,h1), Image.ANTIALIAS )
		img.save(fname, optimize=True, quality=95)

