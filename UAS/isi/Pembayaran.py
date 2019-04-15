from texttable import Texttable
def bayar():
    table= Texttable ()
    jawab1 = "y"
    no=0
    name=[]
    nim=[]
    kelas=[]
    membayar_semester=[]
    membayar_seminar=[]
    membayar_kas=[]
    membayar_uts=[]
    membayar_uas=[]
    admin=[]
    
    
     
    
    while(jawab1 == "y"):
        nama=(input("\n\n\tMasukan Nama  : "))
        nim=(input("\tMasukan NIM   : "))
        kelas=(input("\tMasukan Kelas : "))
        pilih = (input("\nApakah anda ingin membayar semester (y/t) ? "))
        if pilih == 'y':
            membayar_semester =int(input("untuk berapa bulan ? "))
            d_membayar_semester = 'membayar_SEMESTER'
            membayar_semester=500000*membayar_semester
            print("=====================================================")
        else :
            sem_ = ''
            sem=0
            print("=====================================================")
        pilih = (input("\ningin membayar UTS (y/t) ? "))
        if  pilih == 'y':
            membayar_uts =int(input("ingin berapa bulan ? "))
            d_membayar_uts  = 'membayar_UTS'
            membayar_uts=50000*membayar_uts
            print("=====================================================")
        else :
            membayar_uts_ = ''
            membayar_uts=0
            print("=====================================================")
        pilih = (input("\ningin membayar UAS (y/t) ? "))
        if  pilih == 'y':
            membayar_uas =int(input("ingin berapa bulan ? "))
            d_membayar_uas  = 'membayar_UAS'
            membayar_uas=500000*membayar_uas
            print("=====================================================")
        else :
            membayar_uas_ = ''
            membayar_uas=0
            print("=====================================================")
        pilih = (input("\ningin membayar seminar  (y/t) ? "))
        if  pilih == 'y':
            membayar_seminar  = 'membayar_seminar'
            membayar_seminar=100000
            print("=====================================================")
        else :
            membayar_seminar = ''
            membayar_seminar=0
            print("=====================================================")
        pilih = (input("\ningin bayar KAS Bulanan (y/t) ? "))
        if  pilih == 'y':
            membayar_kas  = 'membayar_KAS'
            membayar_kas=20000
            print("=====================================================")
        else :
            membayar_kas = ''
            membayar_kas=0
            print("=====================================================")
        pilih = (input("\nAnda akan dikenakan admin wajib (Y)? "))
        if  pilih == 'y':
            admin  = 'ADMIN'
            admin=5000
            print("=====================================================")
        else :
            admin = ''
            admin=0
            print("=====================================================")

        total_bayar = membayar_semester+membayar_seminar+membayar_kas+membayar_uts+membayar_uas+admin
        table.add_rows([['NAMA','NIM','KELAS','SEMESTER','SEMINAR','KAS','UTS','UAS','TOTAL'],
                        [nama ,nim ,kelas ,membayar_semester , membayar_seminar  ,  membayar_kas  , membayar_uts  , membayar_uas,total_bayar  ]])
        print("")
        print("")
        print("")
        print("Total Rincian Yang Dibayar")     
        print (table.draw())
        jawab1 = input("\n  Tambahkan Data Pembayaran (y/t)? ") ; print("")
