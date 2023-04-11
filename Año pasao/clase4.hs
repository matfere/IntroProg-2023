--toria :: Int -> Int
sumatoria n | n == 1 = n
            | otherwise = sumatoria(n-1) + n

sumatoria1 :: Int -> Int
sumatoria1 n | n == 0 = 1
             | otherwise = 2 ^ n + sumatoria1(n-1)

sumatoria2 :: Int -> Float -> Float
sumatoria2 n q | n == 1 = q
               | otherwise = q ^ n + sumatoria2(n-1) q

factorial :: Int -> Int
factorial n | n == 0 = 1
            | n>0 = n * factorial(n-1)

eAprox :: Int -> Float
eAprox n | n==0 = 1
         | otherwise = 1 / (fromIntegral (factorial n)) + eAprox (n-1)
