class Mobile_Legend:
    def __init__(self, inputNama, inputKuat, inputRank):
        self.nama = inputNama
        self.kekuatan = inputKuat
        self.Rank = inputRank

Hero1 = Mobile_Legend("Balmond", "Fighter", "epic")
Hero2 = Mobile_Legend("Layla", "MM", "Master")

print (Hero1.Rank)
