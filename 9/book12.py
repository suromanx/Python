class Alpha:
    def __init__(self,val):
        self.value = val

    def __eq__(self, val):
        print("Alpha: 'equals '")
        return self.value == val

    def __ne__(self, val):
        print("Alpha: 'not equals '")
        return self.value!=val

    def __lt__(self, val):
        print("Alpha: 'less '")
        return self.value<val

    def __ge__(self, val):
        print("Alpha: 'more or equals '")
        return self.value>=val

class Bravo:
    def __init__(self,val):
        self.value = val

    def __eq__(self, val):
        print("Bravo: 'equals '")
        return self.value==val

A = Alpha(100)

print('Операции с обьектом А')
print()
print("[01] A==100:", A==100)
print("[02] A!=100:", A != 100)
print("[03] 200==A:", 200 == A)
print("[04] 200!=A:", 200 != A)
print("[05] A<200:", A < 200)
print("[06] 200>A:", 200 > A)
print("[07] A>=200:", A >= 200)
print("[08] 100<=A:", 100 <= A)
B = Bravo(300)
print("   B")
print("[9] B==300:", B == 300)
print("[10] B!=300:", B != 300)
print("[11] 400==B:", 400 == B)
print("  A  B")
print()
print("[12] A==B:", A == B)
print("[13] B!=A:", B != A)
print("[14] A!=B:", A != B)