#KALKUATOR SEDERHANA


def kalkulator():
    

    print('')
    print("===============KALKULATOR SEDERHANA===============")
    print("\t\t PILIH SALAH SATU\n")
    print("\t\t 1.PENJUMLAHAN")
    print("\t\t 2.PENGURANGAN")
    print("\t\t 3.PERKALIAN  ")
    print('\t\t 4.PEMBAGIAN  ')
    print("==================================================")
    print('')
    pilihan = input("PILIH NOMER BERAPA? ")
    
    if pilihan == '1':
        penjumlahan()

    elif pilihan == '2':
        pengurangan()

    elif pilihan == '3':
        perkalian()

    elif pilihan == '4':
        pembagian()

    else :
        print("huhu,nomer yang anda masukan salah")
    muat()    
    
def penjumlahan():
    print("\n\n===============================")
    print("\tPENJUMLAHAN")
    a = int(input('\nMASUKAN NILAI A :'))
    b = int(input('MASUKAN NILAI B :'))
    print("\nHASIL DARI",a,"+",b,"=",(a+b))
    print("===============================")

def pengurangan():
    print("\n\n===============================")
    print("\tPENGURANGAN")
    a = int(input('MASUKAN NILAI A : '))
    b = int(input('MASUKAN NILAI B : '))
    print("HASIL DARI",a,"-",b,"=",(a-b))
    print("===============================")

def perkalian():
    print("\n\n===============================")
    print("\tPERKALIAN")
    a = int(input("MASUKAN NILAI A : "))
    b = int(input("MASUKAN NILAI B : "))
    print("HASIL DARI",a,"X",b,"=",(a*b))
    print("===============================")

def pembagian():
    print("\n\n===============================")
    print("\tPEMBAGIAN")
    a = int(input("MASUKAN NILAI A : "))
    b = int(input("MASUKAN NILAI B : "))
    print("HASIL DARI",a,"% ",b,"=",(a/b))
    print("===============================")
    

def muat():
    muat = input("INGIN BERHITUNG LAGI ? ")
    if muat =='y':
        kalkulator()
    else:
        print("OKE DEH, TRIMAKASIH SUDAH BERKUNJUNG")
        
    


    

    
