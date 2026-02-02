#https://github.com/1Lugi/oop-kalk
class kalkulaator:
    def __init__(self, a, b):
        self.a = a      #1 number
        self.b = b      #2 number

    def liida(self):
        return self.a + self.b      #liitmine

    def lahuta(self):
        return self.a - self.b      #lahutamine

    def korruta(self):
        return self.a * self.b      #korrutamine

    def jaga(self):
        if self.b == 0:
            return "nulliga jagamine pole lubatud"
        return self.a / self.b

    def aste(self):
        return self.a ** self.b

    def ruutjuur(self):
        if self.a < 0:
            return "negatiivse arvu ruutjuurt ei saa arvutada"
        return self.a ** 0.5

    def absoluut(self):
        return abs(self.a)

    def umarda(self):
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


a = float(input("sisesta 1 number: "))
b = float(input("sisesta 2 number: "))

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

    break