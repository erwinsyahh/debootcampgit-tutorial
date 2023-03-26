#Class methods and attributes
class Handphone:
    #Attributes
    storage = 0
    RAM = 0
    def __init__(self, name, merk, warna):
        self.name = name
        self.merk = merk
        self.warna = warna
    #Methods
    def greet(self):
        print("This phone's specs are:", self.name, self.merk, self.warna, self.storage,"GB", self.RAM,"GB")
    def storageram(self, x, y):
        self.storage = x
        self.RAM = y


hp1 = Handphone("Erwin","Samsung","Merah")
hp1.storageram(8,128)
hp1.greet()