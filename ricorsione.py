
a = [1,34,56,78,97,35,65,11,7]

def scorrimi(a) :
    if a :
        print ( a[0] )
        scorrimi(a[1:])
    else:
        return

scorrimi(a)