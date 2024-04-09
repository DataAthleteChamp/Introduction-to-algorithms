import random

# Klient
class Klient:
    def __init__(self, typ, zlozonosc):
        self.typ = typ
        self.zlozonosc = zlozonosc
        self.next = None


#  Kolejka - lista jednokierunkowa
class Kolejka:
    def __init__(self):
        self.head = None

    def enqueue(self, klient):
        if not self.head:
            self.head = klient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = klient

    def dequeue(self, typ):
        current = self.head
        previous = None
        while current:
            if current.typ == typ or typ == "E":
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return current
            previous = current
            current = current.next
        return None

    def is_empty(self):
        return self.head is None


# urzad
urzad = [{"typ": "A", "zajetosc": 0} for _ in range(3)] + \
        [{"typ": "B", "zajetosc": 0} for _ in range(3)] + \
        [{"typ": "C", "zajetosc": 0} for _ in range(3)] + \
        [{"typ": "E", "zajetosc": 0}]

# kolejka klientów
kolejka = Kolejka()
for _ in range(40):
    typ = random.choice(["A", "B", "C"])
    zlozonosc = random.randint(1, 4) if typ == "A" else random.randint(5, 8) if typ == "B" else random.randint(9, 12)
    kolejka.enqueue(Klient(typ, zlozonosc))

# symulacja obsługi klientów
iteracje = 0
while not kolejka.is_empty() or any(okienko["zajetosc"] > 0 for okienko in urzad):
    for okienko in urzad:
        if okienko["zajetosc"] > 0:
            okienko["zajetosc"] -= 1
        else:
            klient = kolejka.dequeue(okienko["typ"])
            if klient:
                okienko["zajetosc"] = klient.zlozonosc
                okienko.setdefault("obsz_klienci", 0)
                okienko["obsz_klienci"] += 1
    iteracje += 1


wyniki = {"iteracje": iteracje,
          "obsz_klienci": {i: okienko.get("obsz_klienci", 0) for i, okienko in enumerate(urzad, 1)}}

print(wyniki)
#liczba iteracji = czas
# 3 pierwsze iteracje okienko A -liczba klientów
#  iteracje 3 -6 okienko B -liczba klientów
# iteracje 6-9 okienko C -liczba klientów
# iteracje E okienko E -liczba klientów



# Jako usprawnienie procesu wyszukiwania zadań danego typu w kolejce,
# zasugerowałbym przechowywanie osobnych kolejek dla każdego typu zadania.
# Wtedy, zamiast przeszukiwać całą kolejkę w poszukiwaniu pierwszego klienta z odpowiednim typem zadania,
# okienka mogłyby bezpośrednio i szybko dostęp do klientów z odpowiednimi zadaniami.
# Dzięki temu zmniejszyłaby się ilość operacji koniecznych do znalezienia klienta pasującego do danego typu okienka,
# co przyspieszyłoby proces obsługi.
