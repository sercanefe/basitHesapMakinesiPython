print("""
*******************
      
1. Toplama İşlemi     
      
2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
     
*******************    
      """)
      
a = int(input("1. Sayıyı giriniz: "))
b = int(input("2. Sayıyı giriniz: "))

c = input("İşlemi giriniz (örn: 1): ")

if (c == "1"):
    print("{} ile {}'nin toplamı {}'dir.".format(a,b,a+b))
elif (c == "2"):
    print("{} ile {}'nin farkı {}'dir.".format(a,b,a-b))
elif (c == "3"):
    print("{} ile {}'nin çarpımı {}'dir.".format(a,b,a*b))
elif (c == "4"):
    print("{} ile {}'nin bölümü {}'dir.".format(a,b,a/b))
else:
    print("lütfen 1,2,3 ya da 4 işlemlerinden birini seçiniz.")