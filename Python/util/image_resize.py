
import os,glob,unipath
from math import floor
from PIL import Image




# dir0   = '/Users/todd/GitHub/OpenBook-IntroductionToBiomechanics/Tutorials/src/01-InstallJupyter/img/'


# dir0   = 
dir_root = unipath.Path( os.path.dirname(__file__) ).parent.parent
dir0     = os.path.join(dir_root, 'Tutorials', 'src', '01-InstallJupyter')




# dir0   = '/Users/todd/Downloads/img/'
fnames = glob.glob( os.path.join(dir0, 'img', '*.png' ) )



w1     = 1000

for fname in fnames:
	print(fname)
	img   = Image.open(fname)
	w0,h0 = img.size
	if w0 > w1:
		h1    = floor(w1 * h0/w0)
		img  = img.resize( (w1,h1), Image.ANTIALIAS )
		img.save(fname, optimize=True, quality=95)

