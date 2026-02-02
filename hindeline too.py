class kalkulaator:
    def __init__(self, a, b):
        self.a = a      #esimene number
        self.b = b      #teine number

    def liida(self):
        return self.a + self.b      #liitmine

    def lahuta(self):
        return self.a - self.b      #lahutamine

    def korruta(self):
        return self.a * self.b      #korrutamine

    def jaga(self):
        if self.b == 0:
            return "nulliga jagamine pole lubatud"  #vigade kaitse
        return self.a / self.b      #jagamine

    def aste(self):
        return self.a ** self.b     #astendamine

    def ruutjuur(self):
        #algne funktsioon
        #arvutab esimese arvu ruutjuure
        #kasutades astendamist 0.5-ga
        if self.a < 0:
            return "negatiivse arvu ruutjuurt ei saa arvutada"
        return self.a ** 0.5

    def absoluut(self):
        #esimene lisatud funktsioon
        #kasutab pythonis sisseehitatud abs() funktsiooni
        #kui arv on negatiivne, tehakse see positiivseks
        #kui arv on juba positiivne, jaab see samaks
        return abs(self.a)

    def umarda(self):
        #ja teine lisatud funktsioon
        #kasutab round() funktsiooni
        #umardab arvu lahimasse taisarvu
        #naiteks 2.3 > 2 ja 2.7 > 3
        return round(self.a)


def menu():
    print(
        "\nvali tegevus:"
        "\n1. liitmine"
        "\n2. lahutamine"
        "\n3. korrutamine"
        "\n4. jagamine"
        "\n5. astendamine"
        "\n6. ruutjuur"
        "\n7. absoluutvaartus"
        "\n8. umardamine"
    )


#sisend
a = float(input("sisesta esimene number: "))
b = float(input("sisesta teine number: "))

k = kalkulaator(a, b)

while True:
    menu()
    valik = int(input("sisesta valik: "))

    if valik == 1:
        print("vastus:", k.liida())
    elif valik == 2:
        print("vastus:", k.lahuta())
    elif valik == 3:
        print("vastus:", k.korruta())
    elif valik == 4:
        print("vastus:", k.jaga())
    elif valik == 5:
        print("vastus:", k.aste())
    elif valik == 6:
        print("vastus:", k.ruutjuur())
    elif valik == 7:
        print("vastus:", k.absoluut())
    elif valik == 8:
        print("vastus:", k.umarda())
    else:
        print("vale valik, proovi uuesti")
        continue
