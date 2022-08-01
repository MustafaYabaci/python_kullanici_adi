sys_kullanici_adi="mustafa"
sys_parola="123456"
kullanıcı_adı=input("lütfen kullanıcı adı giriniz : ")
parola=input("lütfen parola giriniz : ")
if kullanıcı_adı == sys_kullanici_adi and parola != sys_parola:
    print("kullanıcı adı dogru fakat parola yanlış")
elif(kullanıcı_adı!= sys_kullanici_adi and parola ==sys_parola):
    print("kullanıcı adı hatalı fakat parola dogru")
elif(kullanıcı_adı!= sys_kullanici_adi and parola !=sys_parola):
    print("kullanıcı adı hatalı ve parola hatalı")
else:
    print("kullanıcı adı ve parola dogru")