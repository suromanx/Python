class Alpha:
    pass
class Bravo(Alpha):
    pass
class Charlie(Bravo):
    pass
class Delta(Bravo):
    pass
class Echo(Charlie,Delta):
    pass

k=1

for s in Echo.__mro__:
    print("["+str(k)+"]",s.__name__)
    k+=1
