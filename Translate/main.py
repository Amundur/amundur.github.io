import os

ca=[]
en=[]

en_cont = []
etiquetes = ["p", "h", "title", "a", ]

b = 0

ruta = "E:/Scripts/amundur.github.io/"
nova_ruta = "E:/Scripts/amundur.github.io/en_temp/"
fitxers = []
filenames = os.listdir(ruta)

for fn in filenames:
    if ".html" in fn:
        fitxers.append(fn)

# for doc in fitxers:
#     print(doc + ":")
#     with open (doc, "r") as fix:
#         print(fix.read())
#         for linia in fix:
#             for e in etiquetes:
#                 if ("<" + e + " ") in linia or ("<" + e + ">") in linia:
#                     #print(e + ": " + linia)
#                     index_in = linia.find(">")
#                     index_out = linia.rfind("<")
#                     subcadena = linia[index_in+1:(index_out)]
#                     ca.append(subcadena)
#         print(ca)

trad = open("E:/Scripts/amundur.github.io/Translate/trans.csv", "r")
trad_cont = trad.read()
trad_cont = trad_cont.replace("\n", ";")
lang = trad_cont.split(";")

try:
    os.mkdir(nova_ruta)
except:
    print("fuck")

for t in range(len(lang)):
    if t > 1:
        if t%2 == 0:
            ca.append(lang[t])
        else:
            en.append(lang[t])

for doc in fitxers:
    with open(doc, "r") as fix:
        text = fix.read()
        for cat in ca:
            if cat in text:
                if (text.count(cat)) == 1:
                    text = text.replace(cat, en[ca.index(cat)])
                else:
                    for line in text:
                        try:
                            line = line.replace(cat, en[ca.index(cat)])
                        except:
                            text = 
    with open(nova_ruta + doc, "w")as nou_fix:
        nou_fix.write(text)

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
