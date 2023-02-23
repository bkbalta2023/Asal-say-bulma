while True:

    sayı = int(input("Sayı giriniz: "))
    asalmi = True

    if sayı ==1:
        asalmi=False

    for bölen in range(2,sayı):
        if sayı%bölen==0:
            asalmi=False
            break
    if asalmi:
        print("{} asaldır.".format(sayı))
    else:
        print("{} asal değildir.".format(sayı))
