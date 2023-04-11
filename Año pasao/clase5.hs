sumaDDH n 1=1
sumaDDH n k = sumaDDH n (k-1) + a
        where a | mod n k == 0 = k
                | otherwise = 0

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde n k | k == 1 = 1
                      | mod n k == 0 = k
                      | otherwise = menorDivisorDesde n (k+1)

esPrimo :: Int -> Bool
esPrimo n | menorDivisorDesde n 2 == n = True
          | otherwise = False