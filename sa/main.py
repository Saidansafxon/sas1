a=input("1 ta son kiriting: ")
b=input("yana 1 ta son kiriting: ")
if a>b:
    print("Birinchi son katta")
elif a < b:
    print("Ikkinchi son katta")
else:
    print("Ikkalasi teng")

c=int(input("1 ta son kiriting"))
if 18<c :
    print("Balog‘at yoshiga yetgansiz")
elif c<=18 :
    print("siz balogat yoshiga yetmabsiz")
else :
    print("togri javob yoz")

d = float(input("Birinchi sonni kiriting: "))
r = float(input("Ikkinchi sonni kiriting: "))
natija = d > 0 and r > 0
print(natija)

g=input("ismingizni kiriting: ")
l=int(input("yoshingizni kiriting: "))
if 18<=l :
    print("balogat yoshiga etibsiz")
elif 18>l :
    print("balogat yoshiga yetmabsiz")
else:
    print("togri javob yozing")
print("xush kelibsiz, ali")

sa=int(input("bitta son kiriting: "))
sa1=int(input("yana bitta son kiriting: "))
sa2=int(input("yana bitta son kiriting: "))
sa3=sa+sa1+sa2
print(sa3/3)


