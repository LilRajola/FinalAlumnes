def copia_frase(frase, vegades, separador=None):
    """
    Copia la frase un nombre vegades de vegades. Si hi ha un separador, posa'l
    entremig de les còpies.

    >>> copia_frase('No copiaré en un examen', 3)
    'No copiaré en un examenNo copiaré en un examenNo copiaré en un examen'

    >>> copia_frase('No em cal copiar', 4, '!!!')
    'No em cal copiar!!!No em cal copiar!!!No em cal copiar!!!No em cal copiar'
    """
    ulitma_copia = frase
    if separador != None:
        frase = frase + separador
    
    frasefinal = frase * (vegades -1) + ulitma_copia
    return frasefinal

def copia_posicio_senar(llista):
    """
    Copia els elements en posicio senar d'una llista.

    >>> copia_posicio_senar([1,2,3,4])
    [1,2,2,3,4,4]

    >>> copia_posicio_senar([2,2,3,9,1])
    [2,2,2,3,9,9,1]
    """
    llista_final= []
    posicio = 0
    for elemnt in llista:
        if posicio % 2 == 1:
            llista_final.append(elemnt)
            llista_final.append(elemnt)
        else:
            llista_final.append(elemnt)
        posicio +=1 
    return llista_final
        

def copia_amb_canvis(mot1, diccionari):
    """
    Copia una cadena de caràcters canviant-ne les claus del diccionari pels
    corresponents valors.

    >>> copia_amb_canvis('casa', {'a':'d'})
    'cdsd'

    >>> copia_amb_canvis('zupar', {'z':'s', 'u':'o'})
    'sopar'
    """
    paraula = ''
    contador = 0
    
    for lletra in mot1:
        for traduccio in diccionari:
            if traduccio == lletra:
                paraula += diccionari[traduccio]
            else:
                contador += 1
        if contador == len(diccionari):
            paraula += lletra
        contador  = 0
    return paraula
   

def corregeix(paraula, paraules):
    """
    Donada una paraula i una llista de paraules, canvia la paraula per l'element
    de paraules amb una distància de hamming més petita respecte la paraula. En
    cas que siguin de diferents longituds, tingues en compte només tants
    caràcters com tingui la paraula més curta de la parella a comparar.

    >>> corregeix('peça', ['puça', 'passa'])
    'puça'

    >>> corregeix('exàmen', ['exemple','examen','eixelebrat','examina'])
    'examen'
    """
    
