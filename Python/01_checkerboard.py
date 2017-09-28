shakkiRivi = []

ruutuMaaraRows = int(input())
ruutuMaaraCols = int(input())

ruudunKorkeus = int(input())
ruudunLeveys = int(input())

for r in range(0,ruutuMaaraRows):
    for z in range(0,ruudunKorkeus):
        #shakkirivi tyhjennetään ennen täyttöä
        shakkiRivi = []
        for y in range(0,ruutuMaaraCols):
            for x in range(0,ruudunLeveys):
                #Jos Rivi = Parillinen ja Ruutu = Parillinen tai Rivi = Pariton ja Ruutu = Pariton
                if ((r % 2 == 0 and y % 2 == 0) or (r % 2 != 0 and y % 2 != 0)):
                    shakkiRivi.append(" ")
                #Jos Rivi = Parillinen ja Ruutu = Pariton, tai Rivi = Pariton ja Ruutu = Parillinen
                if ((r % 2 == 0 and y % 2 != 0) or (r % 2 != 0 and y % 2 == 0)):
                    shakkiRivi.append("#")
        for l in shakkiRivi:
            print(l,end="")
        print()


