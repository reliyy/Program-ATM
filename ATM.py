saldo = 100000 #saldo awal
pin = 123 #pin

def login(cobapin = 0):
    
    if cobapin == 3:
        print("Kesempatan habis") 
        return False
        
    tespin = int(input("Masukkan pin: "))

    if tespin == pin:
        print("Berhasil Masuk")
        return True
    else:
        print("Pin Salah")
        return login(cobapin + 1)

def tartu(saldo):
    while True:
        uang = int(input("Masukkan Nominal yang ingin di tarik: "))
        if uang % 50000 != 0:
           print("uang tidak tersedia")
           continue
        if saldo < uang:
            print("Saldo anda tidak cukup!")
            continue
        else:
          sisa = saldo - uang
          saldo = sisa
          print(f"Sisa Saldo Anda: {sisa}")
          return saldo
        

def setortu(saldo):
    while True:
        uang = int(input("Masukkan Nominal yang ingin di setor: "))
        if uang % 50000 != 0 and uang < 0:
            print("harus kelipatan 50rb dan harus positif")
        else:
            sisa = saldo + uang
            saldo = sisa
            print(f"Sisa Saldo Anda: {sisa}")
            return saldo


#Fungsi Menu Atm 
def menuatm():
    print("================ATM RUSAK================")
    print("1.Check Saldo \n2.Tarik Tunai \n3.Setor Tunai \n4.Cancel")


#Alur        
if login() == True:
    while True:
        menuatm()
        menu = int(input("Pilih Menu: "))

        if menu == 1:
            print(f"Sisa Saldo Anda: {saldo}")
            continue
        
        elif menu == 2: 
            saldo = tartu(saldo)

        elif menu == 3:
            saldo = setortu(saldo)

        elif menu == 4:
            print("Terimakasih sudah memakai jasa kami :)")
            break
        
        else:
            print("Pilihan tidak ada di system")
            continue
else:
    print("program selesai")



        
    
  
    
