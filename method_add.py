class SuperStr(str):
    def __init__(self, chaine) :
        self.chaine = chaine
    
    def __add__(self, mot):
        return SuperStr(f"{self.chaine} {mot}")
                        
s = SuperStr("Bonjour")

print(s + "tout" + "le" + "monde")


