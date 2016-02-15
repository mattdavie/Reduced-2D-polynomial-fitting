# Reduced-2D-polynomial-fitting
Fitting too many cross-terms in your polynomials? Want to fit fewer?
Fitting large 2d polynomials has a lot of cross-terms which can lead to irritating degeneracy in your solutions, lack of convergence in mcmc simulations etc. Nobody really wants this, and whilst an iterative approach where one sequentially omits low magnitude cross-terms and then refits would be possible, it is unpleasantly inefficient. This is a customisable, if blunt approach.

For example: fitting up to x**5 * y**5 would include 36 coefficients, if you were to trim cross-terms such that no cross term had both indices as 2 or greater there yould be optimising over only 16 coefficients.
