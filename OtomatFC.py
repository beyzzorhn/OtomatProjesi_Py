# Urun1=1.25, Urun2=3.45, Urun3=5.20, Urun4=8.80 olsun. Ürün sayısı arttırılabilir.
def bakiye(x,y):
    if (y > x):
        print("Bakiye yetersiz. Para iadesi yapiliyor...")
        iade = x
        return iade        
    else:
        print(a, "veriliyor...")
        paraustu = x - y
        print("Para ustu:", (paraustu/100), "Tl")
        return paraustu
    
def hesap(z):
    if (z > 0):
        birTl = int(z/100)
        print(birTl, "tane 1 TL")
        z = z%100
        elli = int(z/50)
        print(elli, "tane 50 kurus")
        z = z%50
        yirmibes = int(z/25)
        print(yirmibes, "tane 25 kurus")
        z = z%25
        on = int(z/10)
        print(on, "tane 10 kurus")
        z = z%10
        bes = int(z/5)
        print(bes, "tane 5 kurus")
        print("Para iadesi yapildi. Tesekkurler...")
    elif (z == 0):
        print("Tesekkurler...")
    
while True:
    print("Hos geldiniz...")
    tl = float(input("Lutfen para girisi yapiniz: "))
    secim = input("Lutfen urun secimi yapiniz: ")
    kurus = int(tl*100)
    
    match secim:
        case "1":
            urun= 125
            a = "Urun1"
        case "2":
            urun= 345
            a = "Urun2"
        case "3":
            urun= 520
            a = "Urun3"
        case "4":
            a = "Urun4"
            urun= 880
    hesap(bakiye(kurus, urun))