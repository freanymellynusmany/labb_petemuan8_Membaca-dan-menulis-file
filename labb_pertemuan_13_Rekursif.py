#Freany Mellyn Usmany
#71200644
#Universitas Kristen duta wacana

#pada SMA taruna Bhakti melakukan upacara tetapi siswa dilarang untuk berdekatan, penjumlahan dari 
#beberapa bilangan yang ada pada sebuah list pun harus menjaga jarak. Bilangan yang 
# ada pada sebuah list dapat ditambahkan satu sama lain untuk mencapai target yang ingin dicapai, namun apabila 
#bilangan berada pada posisi yang berdekatan maka bilangan tersebut tidak dapat 
#dijumlahkan. Buatlah program rekursif yang dapat memenuhi syarat-syarat tersebut 
#sehingga upacar yang dilakasanakan dengan baik. Output yang diharapkan hanyalah 
#True ataupun False

def jagajarak (awal, listnya, hasil):
    if(hasil == 0):
        return True
    if(awal >= len(listnya)):
        return False
    if(jagajarak(awal+2, listnya, hasil - listnya[awal])):
        return True
    return jagajarak(awal + 1, listnya , hasil)

print(jagajarak(0, [5,7,10,4], 18))
print(jagajarak(0, [5,7,10,4], 17))
print(jagajarak(0, [5,7,10,4], 9))
print(jagajarak(0, [5,7,10,4], 18))