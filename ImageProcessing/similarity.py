import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d

def get(i):
	data = imread('im%s.jpg' % i)
	data = sp.inner(data, [299, 587, 114]) / 1000.0
	return (data - data.mean()) / data.std()

im1 = get(1)
im2 = get(2)
im3 = get(3)

#c11 = c2d(im1, im1, mode='same') 
c12 = c2d(im1, im2, mode='same')
#c13 = c2d(im1, im3, mode='same')
#c23 = c2d(im2, im3, mode='same')
#c11.max(), c12.max(), c13.max(), c23.max()
print c12.max()

