def nilai():
    
    from texttable import Texttable
    table = Texttable ()

    jawab = "y"
    nol = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []

    while(jawab == "y"):
          nama.append(input("\nMasukan Nama : "))
          nim.append(input("\nMasukan Nim : "))
          nilai_tugas.append(input("\nMasukan Nilai Tugas : "))
          nilai_uts.append(input("\nMasukan Nilai UTS :"))
          nilai_uas.append(input("\nMasukan Nilai UAS :"))
          jawab = input("\nTambah DAta (y/n)? ")
          nol +=1
    for f in range(nol):
          tugas = int(nilai_tugas[f])
          uts = int(nilai_uts[f])
          uas = int(nilai_uas[f])
          akhir = (tugas*30/100) + (uts*35/100) +(uas*35/100)
          table.set_cols_dtype(['t','t','t','t','t','t','t'])
          table.add_rows([['NO','Nama','NIM','Tugas','Uts','Uas','Akhir'],
                          [f+1, nama[f],nim[f],nilai_tugas[f],nilai_uts[f],nilai_uas[f],akhir]])
    print(table.draw())
              
