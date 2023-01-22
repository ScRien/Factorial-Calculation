def Factorial_Calculation():
    try:
        sayi = int(input("Sayı giriniz: "))
    except ValueError:
        print("Lütfen Sayı giriniz!")
        SayiAl()
        
    sonuc = 1

    while sayi > 0:
        sonuc = sonuc * sayi
        sayi -= 1
        print("Sonuç: {}".format(sonuc))
        
Factorial_Calculation()

