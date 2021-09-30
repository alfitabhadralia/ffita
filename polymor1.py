class Sapi: 
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Moo, perkenalkan nama saya", self.nama, "umur saya", self.umur, "tahun")

class Serigala:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Aauummmnggg, perkenalkan nama saya", self.nama, "umur saya", self.umur, "tahun")
    
sapi1 = Sapi("Jer", 3)
serigala1 = Serigala("Bounce", 4)

for hewan in (sapi1, serigala1):
    hewan.bersuara()
     