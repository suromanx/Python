class Alpha:
    def __getattr__(self, name):
        return len(name)

class Bravo: