#Freany mellyn Usmany
#71200644
# Universitas kristen Duta Wacana

#Putri adalah seorang mahasiswa tingkat akhir di Universitas kristen Duta Wacana,ia disuruh untuk membuat tipe 
#data yang berbentuk dictionary dan dictionary tersebut berisi data daftar mahasiswa yang mengambil mata 
#kuliah tertentu, pastinya ada mahasiswa yang mengambil lebih dari satu mata kuliah tugas anda adalah 
#buatlah program yang dapat menampilkan jumlah semua mahasiswa yang sedang mengambil mata kuliah

def daftar_mahasiswa(data):
    list1 = list()
    list2 = list()
    for k,v in data.items():
        list1.append(v)
    for x in list1 :
        for y in x:
            list2.append(y)
    set1 =set(list2)
    print(len(set1))

data = {
    'Imk':['Putri', 'Tiur', 'Diky', 'ana'],
    'Prajarkom':['Tiur', 'Putri', 'Ana', 'Wlliam'],
    'Praalpro':['Diky', 'Putri', 'Tiur', 'Ana']
}
daftar_mahasiswa(data)
