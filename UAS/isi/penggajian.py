def gaji():
    from texttable import Texttable
    table = Texttable ()

    jawab = 'y'
    no = 0
    name = []
    jabatan = []
    gaji = []

    while  (jawab == 'y'):
           name.append(input('MASUKAN NAMA ANDA : '))
           print("1.KOKI")
           print("2.PROGRAMER")
           print("3.DOKTER")
           print("4.DISAIN")
           print("5.TNI")
           jab = input('MASUKAN JABATAN ANDA : ')
           jabatan.append(jab)

           if (jab == 'koki'):
               gaji.append('Rp.10.000.000')
               jawab = input('TAMBAH DATA : ')
               no +=1

           elif(jab == 'programer'):
               gaji.append('Rp.15.000.000')
               jawab = input('TAMBAH DATA : ')
               no +=1

           elif(jab == 'dokter'):
               gaji.append('Rp.20.000.000')
               jawab = input('TAMBAH DATA : ')
               no +=1

           elif (jab == 'disain'):
               gaji.append('Rp.25.000.000')
               jawab = input('TAMBAH DATA : ')
               no +=1

           elif (jab == 'tni'):
               gaji.append('Rp.10.000.000')
               jawab = input('TAMBAH DATA : ')
               no +=1

           else :
               print('JABATAN TIDAK DI TEMUKAN')
               from Ready import ready

    for f in range(no):
        table.set_cols_dtype(['i','t','t','t'])
        table.add_rows([['NO','NAME','JABATAN','GAJI'],
                      [f+1,name[f],jabatan[f],gaji[f]]])
        print(table.draw())

























        
