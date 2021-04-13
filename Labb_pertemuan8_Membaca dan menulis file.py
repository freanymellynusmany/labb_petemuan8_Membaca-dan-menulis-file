#freany mellyn usmany
#71200644
#Universitas Kristen Duta Wacana

#pada hari minggu gereja mengadakan lomba memperingati Hut Gereja Elim yang ke 50 yaitu dengan mengadakan lomba sepak bola 
#dan pada remaja digereja tersebut wajib mengikutinya,terdapat 4 tim yang bermain yaitu tim merah,biru,ungu,hijau namun pada 
#perlombaan tersebut tim hijau kalah dan tersisa tim merah,biru,dan ungu scorenya dilihat pada data text, carilah nilai 
#atau score terbesar dari ketiga tim tersebut?

handle = open("D:\data.txt")
handle2 = handle.read()
handle2 = handle2.split(',')

def main():
    # cetak judul program
    print('program menentukan nilai maksimum tiga bilangan Cara Pertama')
 
    # input user
    a = int(input('masukan score tim merah   : '))
    b = int(input('masukan score tim biru      : '))
    c = int(input('masukan score tim ungu     : '))
    
    # menentukan nilai terbesar
    if a > b:
        if a > c:
            maks = a
    else:
        if b > c:
            maks = b
        else:
            maks = c
 
 
    print('score yang terbesar adalah: %d' % maks)
         
if __name__=='__main__':
    main()