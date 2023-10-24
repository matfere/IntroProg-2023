--Problema: relacionesValidas


todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True 
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False 
hayRepetidos (x:xs) | pertenece x xs = True
                      | otherwise = hayRepetidos xs

testDist = [1..10]
testIgual = [1,2,3,2,2,3,3,3]

-- Problema relacionesValidas
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((p1,p2):rs) = cadaRelValida && noHayRelRep && relacionesValidas rs
                            where 
                                cadaRelValida = p1 /= p2 
                                noHayRelRep = not (pertenece (p1,p2) rs) && not (pertenece (p2,p1) rs) 

pertenece :: (Eq t) => t -> [t] -> Bool --tipo gen -> bool
pertenece _ [] = False --si no tengo coincidencias no pertenece
pertenece y (x:xs) | y == x = True --me fijo si Y es igual al primer elemento de la seq, si lo es devuelvo True
                   | otherwise = pertenece y xs --si no es igual pruebo con el segundo usando recursion

-- Problema personas
personas :: [(String,String)] -> [String]
personas rs = sacarRepes (personasConRepes rs)

personasConRepes :: [(String,String)] -> [String]
personasConRepes [] = []
personasConRepes ((p1,p2):rs) = p1 : p2 : personas rs

sacarRepes :: (Eq t) => [t] -> [t]
sacarRepes [] = []
sacarRepes (x:xs)
 | pertenece x xs = pasoRecursivo
 | otherwise = x : pasoRecursivo
 where pasoRecursivo = sacarRepes xs
