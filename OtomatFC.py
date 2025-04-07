# ürün1 = 1.25
# ürün2 = 3.45
# ürün3 = 5.20
# ürün4 = 8.80

def bakiye(x,y):
    paraustu = x - y
    print("Bakiye: ", (paraustu/100))
    return paraustu
    
def hesap(z):
    birTl = int(z/100)
    print(birTl, "tane 1 TL")
    z = z%100
    elli = int(z/50)
    print(elli, "tane 50 kuruş")
    z = z%50
    yirmibes = int(z/25)
    print(yirmibes, "tane 25 kuruş")
    z = z%25
    on = int(z/10)
    print(on, "tane 10 kuruş")
    z = z%10
    bes = int(z/5)
    print(bes, "tane 5 kuruş")
    
    
    
print("Hoş geldiniz...")
tl = float(input("Lütfen para girisi yapiniz: "))
secim = input("Lütfen urun secimi yapiniz: ")
kurus = int(tl*100)

match secim:
    case "1":
        print("Urun1 veriliyor.. ")
        urun= 125
    case "2":
        print("Urun2 veriliyor.. ")
        urun= 345
    case "3":
        print("Urun3 veriliyor.. ")
        urun= 520
    case "4":        
        print("Urun4 veriliyor.. ")
        urun= 880

hesap(bakiye(kurus, urun))

