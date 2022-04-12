class Hewan:
  def __init__(self, JenisHewan,NamaHewan ):
    self.JenisHewan = JenisHewan
    self.NamaHewan = NamaHewan
    
class Hewan(Hewan):
  pass

JenisHewan = JenisHewan("Carnivora")
NamaHewan = NamaHewan("Harimau")

print(JenisHewan.NamaHewan, NamaHewan.JenisHewan)
print(JenisHewan.NamaHewan)
