#mapel
senin  =["ke-1 algoritma graf","ke-3 sistem operasi","ke-4 pak","ke-5 praktikum inlan"]
selasa =["ke-2 matematika teknik","ke-4 bahasa indonesia","ke-6 pkn"]
kamis  =["ke-1 IMK","ke-3 logmat ","ke-4 praktekkom"]
jumat  =["ke-2 sistem basis data","ke-4 prakom sistem basis data","ke-6 INLAN"]

scene = input("hi kiko, silahkan masukkan hasil yang ingin anda telusuri : ")
#jadwal
if scene == "senin" :
    for i in range (len(senin)):
        print ("kelas", senin[i])
elif scene == "selasa" :
    for i in range (len(selasa)):
        print ("kelas", selasa[i])
elif scene == "rabu" :
        print ("hari rabu anda tidak ada kelas")
elif scene == "kamis" :
    for i in range (len(kamis)):

        print ("kelas", kamis[i])
elif scene == "jumat" :
    for i in range (len(jumat)):
        print ("kelas", jumat[i])
