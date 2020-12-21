from knjige.knjigeIO import ucitaj_knjige,sacuvaj_knjige

def pretrazi_knjige_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretrazi_knjige_brojevi(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretrazi_knjige():
    print("1. Pretrazi po naslovu")
    print("2. Pretrazi po kategoriji")
    print("3. Pretrazi po autoru")
    print("4. Pretrazi po izdavacu")
    print("5. Pretrazi po ceni")

    stavka = int(input("Izaberite stavku: "))
    knjige = []
    if stavka == 1:
        naslov = input("Unesite naslov: ")
        knjige = pretrazi_knjige_string('naslov', naslov)

    elif stavka == 2:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string('kategorija', kategorija)

    elif stavka == 3:
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_string("autor", autor)

    elif stavka == 4:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretrazi_knjige_string('izdavac', izdavac)

    elif stavka == 5:
        cena = input("Unesite cenu: ")
        knjige = pretrazi_knjige_brojevi("cena", cena)

    else: print("Unesite ponovo zeljenu opciju")


    for knjiga in knjige:
        print(knjiga)



def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp
    return knjige


def prikazi_knjige():
    print("1. Sortiraj po naslovu")
    print("2. Sortiraj po kategoriji")
    print("3. Sortiraj po autoru")
    print("4. Sortiraj po izdavacu")
    print("5. Sortiraj po ceni")

    stavka = int(input("Izaberite stavku: "))

    knjige = []

    if stavka == 1:
        knjige = sortiraj_knjige("naslov")

    elif stavka == 2:
        knjige = sortiraj_knjige("kategorija")

    elif stavka == 3:
        knjige = sortiraj_knjige("autor")

    elif stavka == 4:
        knjige = sortiraj_knjige("izdavac")

    elif stavka == 5:
        knjige = sortiraj_knjige("cena")

    else: print("Unesite ponovo zeljenu opciju")

    for knjiga in knjige:
        print(knjiga)



def dodaj_knjigu():
    knjige=ucitaj_knjige()
    sifra=int(input("Unesi sifru:"))
    naslov=input("Unesi naslov knjige:")
    autor=input("Unesi autra knjige:")
    isbn=input("Unesi isbn:")
    izdavac=input("Unesi izdavaca:")
    godina=int(input("Unesi godinu izdavanja:"))
    cena=float(input("Unesi cenu knjige:"))
    kategorija=input("Unesi kategoriju knjige:")
    novaKnjiga={

        "sifra": sifra,
        "naslov": naslov,
        "autor": autor,
        "isbn": isbn,
        "izdavac": izdavac,
        "godina": godina,
        "cena": cena,
        "kategorija": kategorija

    }
    knjige.append(novaKnjiga)
    sacuvaj_knjige(knjige)




def izmeni_knjigu():
    sifra=int(input("Unesi sifru knjige za menjanje:"))
    knjige = ucitaj_knjige()
    for i in range(0,len(knjige)):
        if knjige[i]["sifra"] == sifra:
            break
    string=input("Unesi novi naslov:")
    if string != "":
        knjige[i]["naslov"]=string

    string=input("Unesi novog autora:")
    if string != "":
        knjige[i]["autor"]=string

    string =input("Unesi novi isbn:")
    if string != "":
        knjige[i]["isbn"] = string

    string = input("Unesi novog izdavaca:")
    if string != "":
        knjige[i]["izdavac"] = string

    string = input("Unesi novu godinu:")
    if string != '':
        knjige[i]["godina"] = int(string)

    string = input("Unesi novu cenu:")
    if string != "":
        knjige[i]["cena"] = int(string)

    string = input("Unesi novu kategoriju:")
    if string != "":
        knjige[i]["kategorija"] = string
    sacuvaj_knjige(knjige)





