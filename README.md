# Reduced-2D-polynomial-fitting
Fitting too many cross-terms in your polynomials? Want to fit fewer?
Fitting large 2d polynomials has a lot of gross-terms which can lead to irritating degeneracy in your solutions, lack of convergence in mcmc simulations etc. Nobody really wants this, and whilst an iterative approach where one sequentially omits low magnitude cross-terms and then refits would be possible, it is unpleasantly inefficient. This is a customisable, if blunt approach.
