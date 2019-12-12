# Primality_tests
 Primality test algorithms I made for fun

 Currently the code That is uploaded is an implimentation of Baillie-PSW primality test.

About Baillie-PSW primality test:
this test is fundamentally a probablistic primality test, however it has been shown that there are no composite primes that gets filtered as prime for n < 2^64.
Baillie-PSW test is made from two weaker primality test (Miller-Rabin test and Lucas test), both test have some pseudoprimes that doesn't get filtered, but the psudoprimes for respective tests are of different residue class.

any n < 2^64

🡇

Miller-Rabbin test ( Psudoprimes of residue class -1 slips through)

🡇

Lucas test (psudoprimes of residue class 1 slips through)

🡇

only primes pass the two filters