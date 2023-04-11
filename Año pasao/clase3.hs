fib :: Int -> Int
fib n | n == 0  = 0
      | n == 1  = 1
      | otherwise = fib(n-1) + fib(n-2)

parteEntera :: Float -> Integer
parteEntera n | n < 1 = 0
              | otherwise = parteEntera(n-1) + 1 

esPar :: Int -> Bool
esPar n | n ==0 = True
        | n ==1 = False
        | otherwise = esPar (n -2)

multiplo :: Integer -> Bool
multiplo n | n ==3 = True
           | n < 3 = False
           | otherwise = multiplo(n-3)
           
sumaImpares :: Int -> Int
sumaImpares n | n == 1 = 1
              | otherwise = (2*n)-1 + sumaImpares(n-1)
 
medioFact :: Int -> Int
medioFact n | n == 1 = 1
            | n == 2 = 2
            | otherwise = n * medioFact(n-2)

sumaDig :: Int -> Int
sumaDig n | n <= 9 = n
          | otherwise =  sumaDig(div n 10) + mod n 10
          

