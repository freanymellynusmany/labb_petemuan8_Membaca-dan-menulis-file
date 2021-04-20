#Freany Mellyn Usmany
#71200644

#Dedi muhammad adalah mahasiswa diuniversitas Gajah Mada dan ia disuruh oleh dosennya membuat list nilai mahasiswa
#dengan Nim,nilai Uts,Nilai Uas dan yang terakhir adalah rata-ratanya

# Input
List_NIM= []
List_UTS= []
List_UAS= []
List_total= []

ulang =int(input("Masukkan jumlah data yang ingin dimasukkan: "))

for i in range(ulang):
    print("*"*50)
    print("data ke - " + str(i+1))
    List_NIM.append(input("Masukkan Nim Anda: "))
    List_UTS.append(int(input("Masukkan Nilai UTS Anda: ")))
    List_UAS.append(int(input("Masukkan Nilai UAS ANDA: ")))

# proses
for i in range(len(List_UAS)):
    List_total.append((List_UAS[i] + List_UTS[i]) / 2)

# cetak
print("="*65)
print("NIM\t\tNilai UTS\tNilai UAS\tRata-rata")
print("="*65)

for i in range(ulang):
    print("%s\t%i\t\t%i\t\t%.2f"%(List_NIM[i], List_UTS[i], List_UAS[i], List_total[i]))
print("="*65)
