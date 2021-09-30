class Serangga:
    def intro(self):
        print("Di dunia ini ada beberapa type berbeda dari spesies serangga")

    def Antena(self):
        print("Hampir semua serangga mempunyai antena, namun ada beberapa yang berbeda jenisnya")

class Lebah(Serangga):
    def antena(self):
        print("Lebah mempunyai sepasang antena")

class Semut(Serangga):
    def antena(self):
        print("Semut mempunyai antena yang berbeda jenisnya")


obj_Serangga = Serangga()
obj_Lebah = Lebah()
obj_Semut = Semut()

obj_Serangga.intro()
obj_Serangga.Antena()

print("\n")

obj_Lebah.intro()
obj_Lebah.antena()

print("\n")

obj_Semut.intro()
obj_Semut.antena()

