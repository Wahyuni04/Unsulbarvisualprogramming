class Mahasiswa:
  def __init__(self, Nama, Nim):
    self.Nama = Nama
    self.Nim = Nim
 
  def Mahasiswa(self):
    print(self.Nama, self.Nim)

class Mahasiswa(Mahasiswa):
  pass

x = Mahasiswa("Wahyuni")
x.printNama()
x = Mahasiswa("D0219395")
x.printNim()
