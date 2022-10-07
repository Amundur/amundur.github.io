import os

ca=[]
en=[]

en_cont = []
etiquetes = ["p", "h", "title", "a", ]
linia = ""

ruta = "/Users/anderromeroaldana/Documents/GitHub/amundur.github.io"
fitxers = []
filenames = os.listdir(ruta)

for fn in filenames:
    if ".html" in fn:
        fitxers.append(fn)

for doc in fitxers:
    print(doc + ":")
    with open (doc, "r") as fix:
        for linia in fix:
            for e in etiquetes:
                if ("<" + e + " ") in linia:
                    print("<" + e + " ")
                    print(linia)


# trad = open("/Users/anderromeroaldana/Documents/GitHub/amundur.github.io/Translate/trans.csv", "r")
# trad_cont = trad.read()
# trad_cont = trad_cont.replace("\n", ";")
# lang = trad_cont.split(";")

# for t in range(len(lang)):
#     if t > 1:
#         if t%2 == 0:
#             ca.append(lang[t])
#         else:
#             en.append(lang[t])

# for fn in filenames:
#     if ".html" in fn and fn != "404.html":
#         fitxers.append(fn)

# for doc in fitxers:
#     print(doc + ":")
#     fix = open(doc, "r")
#     cont = fix.read()
#     for c in range(len(ca)):
#         try:
#             en_cont = cont.replace(ca[c], en[c])
#         except:
#             print("fail")
#     print(en_cont)
# print("Hi")
