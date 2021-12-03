#input
lebar = int(input("Masukkan Angka : "))
print()

#rumus penyelesaian
for miya in range (lebar) :
   str(print(" "*(lebar-miya)+" *"*(miya+1)))
    
for deer in range (lebar-1) :
   str(print(" "*(deer+2)+" *"*(lebar-1-deer)))
