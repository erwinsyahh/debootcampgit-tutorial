#Class Inheritance, Polymorphism, Abstraction
from abc import ABC, abstractmethod
class Warga(ABC):
    def __init__(self, NIK:str):
        self.NIK = NIK
    #Abstraction
    @abstractmethod
    def nyoblos(self,pilihan):
        self.pilihan = pilihan
        print(f"{self.status}, {self.NIK} memilih {pilihan}")
        
    def setstatus(self, status = "Status: Warga"):
        self.status = status
        pass

class Satpam(Warga):
    def __init__(self, NIK, satpam_id):
        super().__init__(NIK)
        self.satpam_id = satpam_id
 
    def jaga_tpu(self,tempat):
        print(f"{self.satpam_id} jaga di {tempat}")
        
    def setstatus(self, status = "Status: Satpam"):
        self.status = status
        
    def nyoblos(self,pilihan):
        self.pilihan = pilihan
        print(f"{self.status}, {self.NIK} memilih {pilihan}")
        
class Petugas(Warga):
    def __init__(self, NIK, petugas_id):
        super().__init__(NIK)
        self.petugas_id = petugas_id

    def hitung_suara(self, daftar_suara, tempat):
        self.daftar_suara = daftar_suara
        self.rekap_suara = {}
        self.tempat = tempat
        for suara in daftar_suara:
            if suara in self.rekap_suara:
                self.rekap_suara[suara] += 1
            else:
                self.rekap_suara[suara] = 1                 
        print(f"Hasil rekap suara di {tempat} adalah {self.rekap_suara}")
        
    def setstatus(self, status = "Status: Petugas"):
        self.status = status
        
    def nyoblos(self,pilihan):
        self.pilihan = pilihan
        print(f"{self.status}, {self.NIK} memilih {pilihan}")
        
class TNI(Warga):
    def __init__(self, NIK, TNI_id):
        super().__init__(NIK)
        
    def nyoblos(self, pilihan):
        print(f"{self.NIK}, {self.status} TNI TIDAK WAJIB melakukan pemilihan umum!")
        
    def setstatus(self, status = "Status: TNI"):
        self.status = status
        
    def nyoblos(self,pilihan):
        self.pilihan = pilihan
        print(f"{self.status}, {self.NIK} memilih {pilihan}")
              
class homeless(Warga):
        pass

mukhlis = Satpam("0223456","001")
mukhlis.setstatus()
mukhlis.nyoblos("Mega")
mukhlis.jaga_tpu("Pamekasan")