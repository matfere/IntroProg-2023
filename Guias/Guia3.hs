-- ejercicio 1 (f y g funcionan de la misma forma)
funcion :: Integer -> Integer
funcion f | f == 8 = 16
          | f == 16 = 4
          | f == 131 = 1
          | otherwise = 0

-- ejercicio 2

--a
absoluto :: Integer -> Integer
absoluto n = abs(n)

--b
maxAbsoluto :: Integer -> Integer -> Integer
maxAbsoluto n m | abs(n) > abs(m) = abs(n)
                | abs(n) < abs(m) = abs(m)

--c
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c | a > b && a > c = a
              | b > a && b > c = b
              | c > a && c > b = c

--d
algunoEs0 :: Float -> Float -> Bool
algunoEs0  a b | a == 0 || b == 0 = True
               | otherwise = False

--e
ambosSon0 :: Float -> Float -> Bool
ambosSon0  a b | a == 0 && b == 0 = True
               | otherwise = False

--f
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <=3 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

--g
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c | a == b && a == c = a
                    | a == b = a + c
                    | b == c = a + c
                    | c == a = b + c
                    | otherwise = a + b + c

--h
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y = mod y x == 0

--i
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10 -- mod te da el resto del primer valor dividido el segundo

--j
digitoDecenas :: Integer -> Integer
digitoDecenas n = div (mod n 100) 10 -- div te da el cociente del primer valor dividido el segundo

--Ejercicio 3
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | a == 0 || b == 0 = False
                      | otherwise = mod a b == 0

--Ejercicio 4

--a
prodInt :: (Integer, Integer) -> (Integer,Integer) -> Integer
prodInt a b = (fst a) * (fst b) + (snd a) * (snd b)

--b
todoMenor :: (Integer, Integer) -> (Integer, Integer) -> Bool
todoMenor a b = (fst a) < (fst b) && (snd a) < (snd b)

--c
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos a b = sqrt ((((fst a)-(fst b))^2) + (((snd a)-(snd b))^2))
 
--d
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a,b,c) = a + b + c

--e
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) n | esMultiploDe n a && esMultiploDe n b && esMultiploDe n c = a + b + c
                             | esMultiploDe n a && esMultiploDe n b && esMultiploDe n c == False = a + b
                             | esMultiploDe n a && esMultiploDe n b == False && esMultiploDe n c = a + c
                             | esMultiploDe n a == False && esMultiploDe n b && esMultiploDe n c = b + c
                             | esMultiploDe n a && esMultiploDe n b == False && esMultiploDe n c == False = a
                             | esMultiploDe n a == False && esMultiploDe n b && esMultiploDe n c == False = b 
                             | esMultiploDe n a == False && esMultiploDe n b == False && esMultiploDe n c = c
                             | otherwise = 0

--f
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a,b,c) | esPar a = 1
                     | esPar b = 2
                     | esPar c = 3
                     | otherwise = 4

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

--g
crearPar :: a ->b ->(a, b)
crearPar a b = (a , b)

--h
invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)
