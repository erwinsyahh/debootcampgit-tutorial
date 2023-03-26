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

#Part2
class Handphone:
    def __init__(self, name, merk, warna, storage, RAM, toko="Toped"):
        self.name = name
        self.merk = merk
        self.warna = warna
        self.storage = f"{storage} GB"
        self.RAM = f"{RAM} GB"
        self.toko = toko
    
    def greet(self):
        print(f"Hello, my name is {self.name}")
        #print("This phone's specs are:", self.name, self.merk, self.warna, self.storage, self.RAM, "from", self.toko)
        print(f"This phone's specs are: {self.name} {self.merk} {self.warna} {self.storage} {self.RAM} from {self.toko}")
    
    def merk_length(self):
        return len(self.merk)
    
hp1 = Handphone("Erwin", "Xiaomi", "Black", 256, 16)
hp2 = Handphone("Desy", "Samsung", "White", 128, 8, "Shopee")
hp1.greet()
hp2.greet()
