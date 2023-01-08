# No:20010011520
# Ad Soyad: Akylai Bolotbekova
import random
import sys
# programdan cikis sekli
def finis():
    while True:
        son = int(input("Yeni oyun-1 | Cikis-0\n Seciniz: "))
        if son == 1:
            break
        elif son == 0:
            sys.exit(0)
        else:
            print("Yanlis secim")

puan = 0

while True:
    # alan olusturma
    while True:
        boyut = int(input("En az 10 olacak sekilde alan boyutu giriniz: "))
        if boyut >= 10:
            break
    ekran = []
    for i in range(boyut):
        ekran.append(["?"] * boyut)


    def ekran_gost(ekran):
        print("--------------------\n")
        for satir in ekran:
            for sutun in satir:
                print(sutun, end=" ")
            print("\n")
        print("--------------------")
    ekran_gost(ekran)

    # mayin uretimi
    def rand_konum(ekran):
        return random.randint(1, len(ekran))

    mayinlar = set()
    uzunluk = 0
    while True:
        mayinlar.add((rand_konum(ekran), rand_konum(ekran)))
        uzunluk = len(mayinlar)
        if uzunluk == int((boyut * boyut) * 0.3):
            break
    mayin_list = list(mayinlar)
    #  print(mayin_list)

    # mayinli tarla
    def mayin_tarlasi():
        global mayin_list
        for i in mayin_list:
            # mayinlar uretildigi konumlarin bir artililarina yerlestirildigi icin
            ekran[i[0] - 1][i[1] - 1] = "x"
        return ekran

    # oynama
    while True:
        modum = int(input("Acik mod=1 | Gizli mod=0\n Oynamak istediginiz mod: "))
        if modum == 1 or modum == 0:
            break
        else:
            print("Yanlis secim")
    msayi = 0
    secimler = []
    while True:
        # oyundan cikis dongusu
        if puan + 1 == int((boyut * boyut) * 0.7):
            print("Tebrikler, oyunu kazandiniz! Puaniniz={}".format(puan + 1))
            puan = 0
            break
        while True:
            # mayin secilmedigi surece oyunu devam ettiren dongu
            satir = int(input("tahmin satir: "))
            sutun = int(input("tahmin sutun: "))
            secim = [satir, sutun]

            if secim in secimler:
                print("Bu tahmin daha once yapilmistir. Tekrar tahmin ediniz ")
                puan -= 1  # kazancagi puan boyutun %70 asmamasi icin
            else:
                secimler.append(secim)
                break
        puan += 1

        # mayin secildiyse
        if tuple(secim) in mayin_list:
            mayin_tarlasi()
            ekran_gost(ekran)
            print("Maalesef kaybettiniz. Puaniniz={}".format(puan))
            puan = 0
            break
        else:
            # bos secildiyse
            if secim[0] == 1 or secim[1] == boyut or secim[0] == boyut or secim[1] == 1:  # kenar ise
                # kose ise
                if secim[0] == 1 and secim[1] == 1:
                    for i in range(2):
                        for j in range(2):
                            if (secim[0] + i, secim[1] + j) in mayin_list:
                                msayi += 1

                elif secim[0] == 1 and secim[1] == boyut:
                    for i in range(2):
                        for j in range(2):
                            if (secim[0] + i, secim[1] - j) in mayin_list:
                                msayi += 1

                elif secim[0] == boyut and secim[1] == 1:
                    for i in range(2):
                        for j in range(2):
                            if (secim[0] - i, secim[1] + j) in mayin_list:
                                msayi += 1

                elif secim[0] == boyut and secim[1] == boyut:
                    for i in range(2):
                        for j in range(2):
                            if (secim[0] - i, secim[1] - j) in mayin_list:
                                msayi += 1

                else:
                    # kenar ama kose degil ise
                    if secim[0] == 1:
                        for i in range(2):
                            for j in range(secim[1] - 1, secim[1] + 2):
                                if (secim[0] + i, j) in mayin_list:
                                    msayi += 1

                    elif secim[1] == 1:
                        for i in range(secim[0] - 1, secim[0] + 2):
                            for j in range(2):
                                if (i, secim[1] + j) in mayin_list:
                                    msayi += 1

                    elif secim[0] == boyut:
                        for i in range(2):
                            for j in range(secim[1] - 1, secim[1] + 2):
                                if (secim[0] - i, j) in mayin_list:
                                    msayi += 1

                    elif secim[1] == boyut:
                        for i in range(secim[0] - 1, secim[0] + 2):
                            for j in range(2):
                                if (i, secim[1] - j) in mayin_list:
                                    msayi += 1

            else:
                # icinde ise
                for i in range(secim[0] - 1, secim[0] + 2):
                    for j in range(secim[1] - 1, secim[1] + 2):
                        if (i, j) in mayin_list:
                            msayi += 1
            print("\n" * 100)
            if modum == 1:
                mayin_tarlasi()
                ekran[secim[0] - 1][secim[1] - 1] = str(msayi)
                ekran_gost(ekran)
            else:  # modum == 0
                ekran[secim[0] - 1][secim[1] - 1] = str(msayi)
                ekran_gost(ekran)
            msayi=0
    finis()