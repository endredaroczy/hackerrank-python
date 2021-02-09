def countFromBegining(p):
    if p % 2 == 0:
        return int(p/2)
    else:
        return int((p-1)/2)

def countFromEnd(n, p):
    if p % 2 != 0:
        closestEvenToActual = p-1
    else:
        closestEvenToActual = p
    
    if n % 2 != 0:
        closestEvenToEnd = n-1
    else:
        closestEvenToEnd = n
    
    if closestEvenToEnd/closestEvenToActual == 1:
        return 0
    else:
        return  int(math.floor(closestEvenToEnd/closestEvenToActual))
    
    
def pageCount(n, p):
    fromBegining = countFromBegining(p)
    fromEnd = countFromEnd(n, p)
    if fromBegining >= fromEnd:
        return fromEnd
    else:
        return fromBegining