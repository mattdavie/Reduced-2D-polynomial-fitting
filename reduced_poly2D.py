import numpy as np
import itertools


def reducedpolyfit2D(x,y,z,ord=5,crosslim=2):
	#ord will fit up to x**(ord) * y**(ord)
	#to your x,y,z dataset (yes they all should be the same length)
	#and cull cross terms where both powers >= crosslim
	ncols=(ord+1)**2
	G=np.zeros((x.size,ncols))
	ij=itertools.product(range(ord+1),range(ord+1))
	for ind,(i,j) in enumerate(ij):
		G[:,ind]=x**i * y**j * (i<crosslim or j<crosslim)
	m,_,_,_=np.linalg.lstsq(G,z)
	return m
	
def reducedpolyval2D(x,y,m,crosslim=2):
	#will return the value of your fitted polynomial whose coefficients are m
	#at coordinates (x,y) again limiting crossterms as before
	ord=int(np.sqrt(len(m)))-1
	ij=itertools.product(range(ord+1),range(ord+1))
	z=np.zeros_like(x)
	for coeff,(i,j) in zip (m, ij):
		#print i,j,coeff #uncomment for testing/display purposes
		z+=coeff* x**i * y**j * (i<crosslim or j<crosslim)
	return z
