from isi.kalkulator import kalkulator 
from isi.penilaian import nilai
from isi.Pembayaran import bayar
from isi.penggajian import gaji 

def ready():
    print("===============LOGIN==============")
    user = input("\tID : ")
    password = input("\tPassword : ")
    print("==================================")
    if user == 'admin'and password == 'admin':
        print("\tLOGIN ANDA BERHASIL")
        print("==================================\n\n")
        daftar()
    else :
        print("\tGAGAL DALAM LOGIN")
        print("==================================\n\n")
        ready()

def daftar():
    print("|======================================|")
    print("\t\tDAFTAR ISI     ")
    print("\t1.KALKULATOR     ")
    print("\t2.NILAI          ")
    print("\t3.GAJI           ")
    print("\t4.PEMBAYARAN     ")
    print("|======================================|")
    pilihan = input(" PILIH DAFTAR ISI : ")

    if pilihan == '1':
        kalkulator()
    elif pilihan == '2':
        nilai()
    elif pilihan == '3':
        gaji()
    elif pilihan == '4':
        bayar()
    else:
        print("NOMER YANG ANDA MASUKAN SALAH")
    nambah()

def nambah():
    nambah = input("INGIN MENGULANG : ")
    if nambah =='y':
        daftar()
    else:
        print("TRIMAKASIH SUDAH BERKUNJUNG")
        
    
        
ready()

