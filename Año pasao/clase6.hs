sumatoria :: [Integer] -> Integer
sumatoria n | n == [] = 0
            | otherwise = head n + sumatoria(tail n)

longitud :: [Integer] -> Integer
longitud n | n == [] = 0
           | otherwise = 1 + longitud(tail n)

pertenece :: Integer -> [Integer] -> Bool
pertenece e l | l == [] = False
              | e == head(l) = True
              | otherwise = pertenece e (tail(l))
sumatoriapm :: [Int] -> Int
sumatoriapm (x:xs) = x + sumatoriapm xs

productoria :: [Int] -> Int
productoria n | n == [] = 1
              | otherwise = head(n) * (productoria (tail n))

sumarN :: Int -> [Int] -> [Int]
sumarN e [] = []
sumarN e (x:xs) = (e+x) : (sumarN e xs)     

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (sumarElUltimo(xs)) (x:xs)
