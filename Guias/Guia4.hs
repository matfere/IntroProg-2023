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
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n <= 9 = True
                      | div (mod n 100) 10 == mod n 10 = todosDigitosIguales (div n 10)
                      | otherwise = False

--Ejercicio 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n k | k == cantDigitos n = mod n 10
                 | otherwise = iesimoDigito (div n 10) k

cantDigitos :: Integer -> Integer
cantDigitos i | i == 1 = 1
              | i == 0 = 1
              | otherwise = 1 + cantDigitos (div i 10) 

--Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua n | n == (numInvertido n) = True
            | otherwise = False

numInvertido :: Integer -> Integer
numInvertido n = numInvertidoAux n 0

numInvertidoAux :: Integer -> Integer -> Integer
numInvertidoAux n r | n == 0 = r
                    | otherwise = numInvertidoAux (n `div` 10) (r * 10 + n `mod` 10)

--Ejercicio 10
    --todas fueron hechas una vez con recursión y otra sin
    --no tome en cuenta que q ∈ R, pero la resolucion es la misma

--a
f1R :: Integer -> Integer
f1R n | n == 0 = 1
      | otherwise = 2^n + f1R (n-1)

f1 :: Integer -> Integer
f1 n = 2^(n+1) -1

--b
f2R :: Integer -> Integer -> Integer
f2R n q | n == 0 = 1
        | otherwise = q^n + f2R (n-1) q

f2 :: Integer -> Integer -> Integer
f2 n q | q == 1 = n
       | otherwise =  div (q ^(n+1) -2) (q-1) + 1

--c

