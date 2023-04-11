
g x y = x*x + y 

doble x = 2*x

suma x y = x + y

normaVectorial x1 x2 = sqrt(x1**2 + x2**2)

funcionConstante8 x = 8

-- Comentarios

--Patern Matching

maximo :: Int -> Int -> Int -- asignaturas, :t funcion
maximo x y | x >= y = x 
           | otherwise = y
           
f1 n | n >= 3 = 5

f 0 = 1

f n = 0

absoluto n = abs(n)

maximoAbsoluto x y = maximo (absoluto x ) (absoluto y)

maximo3 x y z = maximo (maximo x y) z

algunoEs0A x y = x == 0 || y == 0

algunoEs0B x y | x == 0 || y == 0 = True
               | otherwise = False
               
ambosSon0A x y = x == 0 && y == 0

ambosSon0B x y | x == 0 && y == 0  = True
               | otherwise = False
               
esMultiploDe x y = mod y x == 0

digitoUnidades n = mod n 10 -- mod te da el resto del primer valor dividido el segundo

digitoDecenas n = div (mod n 100) 10 -- div te da el cociente del primer valor dividido el segundo
