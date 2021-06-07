#Freany Mellyn Usmany
#71200644
#Universitas Kristen Duta Wacana

#Suatu hari putri diberikan warisan 20 kode togel oleh eyangnya. Beberapa hari lagi akan ada 
#pengumuman pemenang togel berhadiah. Untuk menghemat waktu dan mengisi kegabutan 
#putri, ia ingin menyortir mana saja kode togel yang sesuai dengan format togel. Bantulah ia untuk 
#menyortir menggunakan regex python.
#Format kode togel:
#- Dimuai dengan angka 4, 5 atau 6.
#- Harus berisi tepat 16 digit angka.
#- Harus hanya terdiri atas digit 0 hingga 9.
#- Boleh terdiri dari grup 4 digit angka tetapi harus dipisahkan oleh tanda “-“
#- Tidak boleh menggunakan pemisah seperti spasi, tanda underscore dsb, kecuali Kembali 
#ke poin di atas.
# -Tidak boleh ada 4 atau lebih digit angka yang berulang

import re

def check(card):
    if not re.search("^[456]\d{3}(-?\d{4}){3}$",card) or re.search(r"(\d)\1{3}", re.sub("-", "",card)):
        return False
    return True

for i in range(int(input("Masukkan banyaknya kartu kredit: "))):
    if check(input("Masukkan nomor togel: ")):
        print("Valid")
    else:
        print("Invalid")

#test case
...
5123 - 4567 -8912 - 3456
5123 - 3567 -8912 - 3456
4123356789123456
4123356789123456
61234 - 567 -8912 - 3456
5113 - 3367 -8912 - 3456