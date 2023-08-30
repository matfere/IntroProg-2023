codificar :: [( Char , Char )] -> [ Char ] -> [ Char ]
codificar _ [] = []
codificar codigo ( letra : ys ) = ( codificarLetra codigo letra ): codificar codigo ys
codificarLetra :: [( Char , Char )] -> Char -> Char
-- no hay caso vacio por especificacion
codificarLetra (( f , s ): xs ) letra | letra == f = s
                                      | otherwise = codificarLetra xs letra
