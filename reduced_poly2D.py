import numpy as np
import itertools


def reducedpolyfit2D(x,y,z,ord=6,crosslim=2):
	#ord will fit up to x**(ord-1) * y**(ord-1)
	#and limit cross terms where a both powers > crosslim
	ncols=(ord+1)**2
	G=np.zeros((x.size,ncols))
	ij=itertools.product(range(ord+1),range(ord+1))
	for k,(i,j) in enumerate(ij):
		G[:,k]=x**i * y**j * (i<crosslim or j<crosslim)
	m,_,_,_=np.linalg.lstsq(G,z)
	return m
	
def reducedpolyval2D(x,y,m,crosslim=2):
	#will return the value of your fitted polynomial whose coefficients are m
	#at coordinates (x,y) again limiting crossterms as before
	ord=int(np.sqrt(len(m)))-1
	ij=itertools.product(range(ord+1),range(ord+1))
	z=np.zeros_like(x)
	for a,(i,j) in zip (m, ij):
		print i,j,a
		z+=a* x**i * y**j * (i<crosslim or j<crosslim)
	return z
