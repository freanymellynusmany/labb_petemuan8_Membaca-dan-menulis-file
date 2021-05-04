#Freany Mellyn Usmany
#71200644
# Universitas Kristen Duta Wacana

#putri adalah seorang siswa diSMA YPPK TARUNA DHARMA yang sangat aktif dalam mengikuti tiap lomba-lomba 
#olahraga disekolahnya,akibatnya ia tidak fokus dengan nilai mata pelajaran lainnya yang sangat rendah,
#untuk itu putri meminta untuk membuat program untuk setiap nilai mata pelajarannya....

def hitungnilai(pelajaran) :

    tampungan = dict()
    total = 0
    for namapelajaran in pelajaran :
        print("Masukan nilai mata pelajaran",namapelajaran,': ',end = ' ')
        nilai = int(input())
        tampungan[namapelajaran] = nilai
    
    for key in pelajaran :
        total+=tampungan.get(key)
    print('Nilai rata-rata mata pelajaran anda saat ini adalah :',total/len(pelajaran))

pelajaran = (
    'matematika','bahasa indonesia','pkn','bahasa inggris','agama','ekonomi','ipa','ips','tik')
hitungnilai(pelajaran)