# Giris yapma kontrolü:
print("Giris Yapma Kontrolü:\n")

kullaniciGirisYapmisMi = False

if kullaniciGirisYapmisMi:
    # Eğer kullanıcı Kodlamaio sitesine giriş yapmışsa sağ üst köşede kullanıcının profil fotoğrafı gözüksün.
    print("Profil Fotoğrafı Açılan Kutu")
else:
    # Eğer kullanıcı Kodlamaio sitesine giriş yapmamışsa sağ üst köşede "Giriş Yap" ve "Kayıt Ol" butonları olsun.
    print("Giriş Yap      Kayıt Ol")
print("--------------------")



# Herhangi bir kurs için ödev, değerlendirme ve yoklama kontrolü:
print("Ödev, değerlendirme ve yoklama kontrolü:\n")

odev1YapılmısMı = False
odev2YapılmısMı = True
degerlendirmeYapılmısMı = True
yoklamadaVarmı = False

if odev1YapılmısMı:
    print("Ödev 1 yapılmış") 
else:
    print("Ödev 1 yapılmamış")

if odev2YapılmısMı:
    print("Ödev 2 yapılmış")
else:
    print("Ödev 2 yapılmamış")

if degerlendirmeYapılmısMı:
    print("Değerlendirme yapılmış")
else:
    print("Değerlendirme yapılmamış")

if yoklamadaVarmı:
    print("Derse katılmış")
else:
    print("Derse katılamış")
print("--------------------")