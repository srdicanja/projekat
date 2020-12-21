from korisnici.korisniciIO import ucitaj_korisnike,sacuvaj_korisnike

korisnici = ucitaj_korisnike()
def prijava():



    korisnicko_ime = input("unesite korisnicko ime: ")
    lozinka = input("lozinka: ")

    for korisnik in korisnici:
        if korisnik['korisnicko ime'] == korisnicko_ime and korisnik['lozinka'] == lozinka:
            return korisnik

        return None
def registrujKorisnika():

    korisnIme = input("Unesi Korisnicko ime:")
#x proverava
    x=1
    while x==1:
        x=0
        for kor in korisnici:
            if kor["korisnicko ime"]== korisnIme:
                x=1
                korisnIme = input("Unesi validno korisnicko ime:")

    loz = input("Unesi lozinku:")
    im = input("Unesi ime:")
    prez = input("Unesi prezime:")
    tip = input("Unesi tip korisnika:")
    while (tip!="Menadzer"):
        if tip=="Prodavac":
            break
        tip=input("Unesi validan tip korisnika:")
    novikorisnik = {
        "korisnicko ime": korisnIme,
        "lozinka": loz,
        "ime": im,
        "prezime": prez,
        "tip_korisnika": tip
        }
    korisnici.append(novikorisnik)
    sacuvaj_korisnike(korisnici)


def sortiraj_korisnike(kljuc):
    koris = ucitaj_korisnike()

    for i in range(len(koris)):
        for j in range(len(koris)):
            if koris[i][kljuc] < koris[j][kljuc]:
                temp = koris[i]
                koris[i] = koris[j]
                koris[j] = temp
    return koris


def prikazi_korisnika():
    print("1. Sortiraj po imenu")
    print("2. Sortiraj po prezimenu")
    print("3. Sortiraj po tipu korisnika")

    stavka = int(input("Izaberite stavku: "))

    sortiraniKorisnici = []

    if stavka == 1:
        sortiraniKorisnici = sortiraj_korisnike("ime")

    elif stavka == 2:
        sortiraniKorisnici= sortiraj_korisnike("prezime")

    elif stavka == 3:
        sortiraniKorisnici = sortiraj_korisnike("tip_korisnika")


    else: print("Unesite ponovo zeljenu opciju")

    for koris in sortiraniKorisnici:
        print("'korisnicko ime': ' {} ', 'ime': ' {} ', 'prezime': '{}', 'tip_korisnika': ' {} '".format(koris['korisnicko ime'],koris["ime"],koris["prezime"],koris["tip_korisnika"]))
