from korisnici.korisnici import prijava,registrujKorisnika,prikazi_korisnika
from knjige.knjige import prikazi_knjige, pretrazi_knjige,dodaj_knjigu,izmeni_knjigu

def meni_administrator():
    while True:
        print('\n1. Prikaz knjiga')
        print('2. Pretraga knjiga')
        print('3. Prikaz akcija')
        print('4. Pretraga akcija')
        print('5. Registracija')
        print('6. Prikaz svik korisnika')
        print('7. Dodavanje knjiga')
        print('8. Izmena knjiga')
        print('9. Logicko brisanje knjiga')
        print('10. Kraj')

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()


        elif stavka == 5:
            registrujKorisnika()
        elif stavka == 6:
            prikazi_korisnika()
        elif stavka == 7:
            dodaj_knjigu()
        elif stavka == 8:
            izmeni_knjigu()


        elif stavka == 10:
            return
        else:
            print("Pokusajte ponovo!")



def meni_menadzer():
    while True:
        print('\n1. Prikaz knjiga')
        print('2. Pretraga knjiga')
        print('3. Prikaz akcija')
        print('4. Pretraga akcija')
        print('5. Registracija')
        print('6. Prikaz svih korisnika')
        print('7. Dodavanje knjiga')
        print('8. Izmena knjiga')
        print('9. Logicko brisanje knjiga')
        print('10. Dodavanja akcijske ponude')
        print('11. Kreiranje izvestaja')
        print('12. Kraj')

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()


        elif stavka == 5:
            registrujKorisnika()
        elif stavka == 6:
            prikazi_korisnika()
        elif stavka == 7:
            dodaj_knjigu()
        elif stavka == 8:
            izmeni_knjigu()


        elif stavka == 12:
            return
        else:
            print("Pokusajte ponovo!")


def meni_prodavac():
    while True:
        print('\n1. Prikaz knjiga')
        print('2. Pretraga knjiga')
        print('3. Prikaz akcija')
        print('4. Prodaja knjiga')
        print('5. Dodavanje knjiga')
        print('6. Izmena knjiga')
        print('7. Logicko brisanje knjiga')
        print('8. Kraj')

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()


        elif stavka == 5:
            dodaj_knjigu()
        elif stavka == 6:
            izmeni_knjigu()


        elif stavka == 8:
            return
        else:
            print("Pokusajte ponovo!")




def main():
    ulogovani_korisnik = prijava()

    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator()
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            pass
        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            pass
        else:
            print("Korisnik ima nepoznatu ulogu!")


main()