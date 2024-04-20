class Konyv:

    lokacio = "én könyvtáram"
    def __init__(self,konyv_cim,konyv_ar = 500):
        self.ar = konyv_ar
        self.cim = konyv_cim
    def __str__(self):
        return f"A könyv címe: {self.cim} és ára: {self.ar}"
    def aratNovel(self,ertek):
        self.ar += ertek;

my_konyv = Konyv("haború és béke",200)

print(my_konyv.ar)

other_konyv = Konyv("Működj és működik",6000)

print(other_konyv.cim)

print(my_konyv.lokacio)

my_konyv.aratNovel(20)

print(my_konyv)