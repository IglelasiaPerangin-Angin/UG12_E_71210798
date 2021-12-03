#Judul
beginning = int(input("Masukkan awal deret: "))
ending = int(input("Masukkan ahkir deret: "))

yisunsin = []

#Rumus
if (beginning + 1) % 2 == 0:

    for x in range (beginning+1,ending,2):

        if x % 5 == 0 or x % 9 == 0: continue

        print ( x , end = " " )

#Penyelesaian
else:

    for x in range (beginning, ending, 2):

        if x % 5 == 0 or x % 9 == 0 : continue
            print (x , end = " ")
