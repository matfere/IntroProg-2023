

identidadT :: t -> t
identidadT x = x

primero :: t1 -> t2 -> t1
primero x y = x

constante5 :: t1 -> t2 -> t3 -> Int
constante5 x y z = 5

triple :: Num t => t -> t
triple x = 3 * x

maximo :: Ord t => t -> t -> t
maximo x y | x >= y = x
           | otherwise = y
           

f1 x y z = x ^ y + z >= x + y ^ z


