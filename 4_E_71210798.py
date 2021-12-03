#judul1
print("Test case 1")

a = [3, 20, 100, -35, 50]

#rumus1
def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil

#penyelesaian1
print(a)
print("Nilai terbesar: " , nilai_maksimal(a))
print("Nilai terkecil: " , nilai_minimal(a))

#judul2
print("Test case 2")


b = [3, 20, 90, 35, 75]

#rumus2
def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil

#penyelesaian2
print(b)
print("Nilai terbesar: " , nilai_maksimal(b))
print("Nilai terkecil: " , nilai_minimal(b))
