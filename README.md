# Reduced-2D-polynomial-fitting
Fitting too many cross-terms in your polynomials? Want to fit fewer?
Fitting large 2d polynomials has a lot of cross-terms which can lead to irritating degeneracy in your solutions, lack of convergence in mcmc simulations etc. Nobody really wants this, and whilst an iterative approach where one sequentially omits low magnitude cross-terms and then refits would be possible, it is unpleasantly inefficient. This is a customisable, if blunt approach.

For example: fitting up to x^5 . y^5 would include 36 coefficients, if you were to trim cross-terms such that no cross term had both indices as 2 or greater there you'd be optimising over only 27 coefficients. If trimmed to indices as 1 or greater there would be only 16.


The following is roughly what it would be like if
ord was set to 1 and crosslim was set to 2
One term would be omitted - that of x^2y^2.

|y^2   |xy^2   |0
|y     |xy     |x^2y
|1     |x      |x^2
