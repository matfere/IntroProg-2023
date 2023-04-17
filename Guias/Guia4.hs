--Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci n | n == 0  = 0
            | n == 1  = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

--Ejercicio 2
parteEntera :: Float -> Integer
parteEntera n | n < 1 = 0
              | otherwise = parteEntera(n-1) + 1 

--Ejercicio 3
esDivisible :: Integer -> Integer ->Bool
esDivisible a b | a == 0 = True
                | a < 0 = False
                | otherwise = esDivisible (a-b) b

--Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | otherwise = (2*n)-1 + sumaImpares(n-1)

--Ejercicio 5
medioFact :: Integer -> Integer
medioFact n | n <= 1 = 1
            | otherwise = n * medioFact (n-2)

--Ejercicio 6
sumaDigitos :: Integer ->Integer
sumaDigitos n | n <= 9 = n
              | otherwise =  sumaDigitos(div n 10) + mod n 10

--Ejercicio 7
todosDigitosIguales :: Integer ->Bool
todosDigitosIguales n | div n 10 == mod n 10 = True
                      | otherwise = False
