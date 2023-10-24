{-
hola pelele
te va a ir bien no t preocupes
posta sos inteligente no te nubles con pelotudeces tkm <3
-}
--primero lo facilito, si te parece muy boludo lo q digo aca salteate hasta la linea 34
--TIPOS DE DATOS (ejemplos)
{-
Integer = 1,2,3,4,..
Float = 1.0,0.5,2.1,... (llevan puntos como comas)
Bool = True,False
String = "hola" (las comillas son importantes, son cadenas de Char)
Char = "c" (LAS COMILLAS SON IMPORTANTES)
Generico = esto es medio falopa pero sirve para cualquiera de los anteriores, es eso de (Eq t) => t
-}

----------------------
--Operaciones Basicas
----------------------

suma :: Integer -> Integer --aca le estoy diciendo que va a entrar un entero y me tiene q devolver un entero
suma a = a + 1 -- esto que hice con la suma aplica al resto de las cosas pero me da paja y se q lo sabes asi q me lo voy a meter en el culo

--ESTO ES SUPER UTIL
resto :: Integer -> Integer -> Integer 
resto a b = mod a b --esto marea un poco pero es lo de algebra, tipo si estas dividiendo algo por tres el resto puede ser 0 1 o 2
--el orden es "a" "dividido" "b"

opciones :: Integer -> Integer
opciones a | a > 1 = 0 --si a es mayor a 1 devuelve 0
           | a < 1 = 1 --si es menor devuelve 1
           | otherwise = 2 --en otro caso devuelve 2

---------------------
--recursion
---------------------

{-la idea de esto es ir reduciendo el problema, es como induccion pero al reves-}
sumatoria :: Integer -> Integer
sumatoria 0 = 0 --viste que aca no use las barritas?? bueno esto de usar el igual de una pero varias veces se llama pattern matching
sumatoria a = a + sumatoria (a-1) -- esto va a sumar el actual con el anterior y asi hasta el 0

--Otro Ejemplo
sumatoriaPares :: Integer -> Integer
sumatoriaPares 0 = 0 --caso base con pattern matching
sumatoriaPares a | mod a 2 == 0 = a + sumatoriaPares (a-1) --si es par lo va a sumar a lo que de la seq anterior
                 | otherwise = sumatoriaPares (a-1) --si no es par va a continuar con el anterior

--------------------
--listas y tuplas
--------------------
--parece dificil pero te juro q es re facil

--primero las tuplas
{-
tupla1 = (1,2) -- pueden ser de cualquier tipo

si quiero el primer elem:
elem1 = fst tupla1 -- ahora elem1 tiene el valor 1

si quiero el segundo:
elem2 = snd tupla1
-}
--pero si tengo una tupla mas grande? puedo hacer lo mismo?
--nop, pero puedo tomar un elemento en la posicion, o sea:

cuartoElemento :: (Integer, Integer, Integer, Integer) -> Integer --fijate como declaro la tupla
cuartoElemento (a,b,c,d) = d --es importante que "armes la tupla" al principio, asi podes acceder mas rapido a los elementos

--LISTAS

--algo divertido q podes hacer con esto (cuando tenes numeros) es escribirlas mas rapido:
listaHasta10Rapida = [1..10] --esto es lo mismo que escribir [1,2,3,4,5,6,7,8,9,10]

--OPERADORES
{-
: => es para meter un numero en una lista
++ => es para meter los numeros dentro de una lista en otra lista
(cuando digo numeros quiero decir variables, onda funciona con cualquier cosa mientras sea con una lista. Esto no lo vas a poder hacer con tuplas)
-}

--bueno no se me ocurre como explicar esto rapido asi que voy a hacer varios ejemplos de recursion con listas

paresHasta :: Integer -> [Integer]
paresHasta 0 = []
paresHasta a | mod a 2 == 0 = a : paresHasta (a-1) --fijate que los dos puntitos son como un + o algo asi
             | otherwise = paresHasta (a-1)

pertenece :: (Eq t) => t -> [t] -> Bool --tipo gen -> bool
pertenece _ [] = False --si no tengo coincidencias no pertenece
pertenece y (x:xs) | y == x = True --me fijo si Y es igual al primer elemento de la seq, si lo es devuelvo True
                   | otherwise = pertenece y xs --si no es igual pruebo con el segundo usando recursion

eliminarElemento :: Integer -> [Integer] -> [Integer]
eliminarElemento _ [] = []
eliminarElemento a (x:xs) | a == x = eliminarElemento a xs -- si el elemento es identico al primero de la lista va a volver a llamar a la funcion sin contar al primer elemento
                          | otherwise = x : eliminarElemento a xs -- si no va a meter el elemento una vez que se quede sin elementos la lista

eliminarRepetidos :: [Integer] -> [Integer]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = x : eliminarRepetidos (eliminarElemento x xs) --si el primer elem pertenece al resto de la lista, va a eliminar todos sus clones salvo el mismo que se va a posicionar al frente para cuando la lista quede vacia
                         | otherwise = x : eliminarRepetidos xs --si no esta repetido simplemente va a ir al frente

