import numpy as np
import matplotlib.pyplot as plt
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


def generate_kolejka(n):
    kolejka = []
    for _ in range(n):
        typ = random.choice(["A", "B", "C"])
        zlozonosc = random.randint(1, 4) if typ == "A" else random.randint(5, 8) if typ == "B" else random.randint(9, 12)
        kolejka.append(Klient(typ, zlozonosc))
    return kolejka

def symuluj_obsluge(urzad_config, kolejka):
    urzad = [{"typ": typ, "zajetosc": 0} for typ in urzad_config]
    kolejka = generate_kolejka(30)
    iteracje = 0
    while kolejka or any(okienko["zajetosc"] > 0 for okienko in urzad):
        for okienko in urzad:
            if okienko["zajetosc"] > 0:
                okienko["zajetosc"] -= 1
            elif kolejka:
                for i, klient in enumerate(kolejka):
                    if klient.typ == okienko["typ"] or okienko["typ"] == "E":
                        okienko["zajetosc"] = klient.zlozonosc
                        del kolejka[i]
                        break
        iteracje += 1
    return iteracje

urzedu_konfiguracje = [
    "AAA" + "BBB" + "CCC",  # 3A, 3B, 3C
    "AA" + "BB" + "CC" + "EEE",  # 2A, 2B, 2C, 3E
    "A" + "BB" + "CCC" + "E"  # 1A, 2B, 3C, 1E
]

# testowanie
wyniki = []
for konfiguracja in urzedu_konfiguracje:
    czas_obslugi = symuluj_obsluge(konfiguracja, generate_kolejka(30))
    wyniki.append(czas_obslugi)


testy = 100
czas_obslugi_konfiguracji = {konfiguracja: [] for konfiguracja in urzedu_konfiguracje}
for _ in range(testy):
    for konfiguracja in urzedu_konfiguracje:
        czas_obslugi_konfiguracji[konfiguracja].append(symuluj_obsluge(konfiguracja, generate_kolejka(30)))


srednie_czasy = {konfiguracja: np.mean(czasy) for konfiguracja, czasy in czas_obslugi_konfiguracji.items()}


plt.figure(figsize=(10, 7))
for i, (konfiguracja, czasy) in enumerate(czas_obslugi_konfiguracji.items(), start=1):
    plt.subplot(len(urzedu_konfiguracje), 1, i)
    plt.hist(czasy, label=f"Konfiguracja {konfiguracja}", alpha=0.7, bins=15)
    plt.title(f"Histogram czasu obsługi - Konfiguracja {konfiguracja}")
    plt.xlabel("Czas obsługi")
    plt.ylabel("Liczba wystąpień")
    plt.legend()

plt.tight_layout()
plt.show()

print(srednie_czasy)
