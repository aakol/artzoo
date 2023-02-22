#!/bin/python3
import tkinter as tk
from ftplib import FTP
from tkinter import *
import codecs

def wysylanie():
    aaa=tekst.index('end').split(".")
    bbb=int(aaa[0])
    des=tekst.get("1.0","4.0")
    
    plik = codecs.open('index.html', 'w', 'utf-8')
    print("otwarcie pliku")
    plik.write('<!doctype html public "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><title>ArtZoo Sosabowskiego ryby sklep zoologiczny akwarystyczny Białystok</title><link rel="shortcut icon" href=​"favicon.ico" type="image/x-icon"><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="description" content="sklep zoologiczny z rybami Bialystok Sosabowskiego tesco akwarystyka '+ des +' podlaskie ArtZoo"><meta name=" abstract " content="akwarystyka białystok ryby rybki akwariowe rosliny bialystok sklep akwarystyczny zwierzęta wodne "> <meta name="keywords" content="ryby akwariowe,ryby slodkowodne,zooart,akwarium,krewetka, sklep zoologiczny, art zoo, zoologia, zwierzęta, podlasie, akcesoria akwariowe, rosliny akwariowe"> <meta name="author" content="Art Zoo"><meta http-equiv="Content-Language" content="pl" /><meta name="robots" content="index, follow" /><meta name="GOOGLEBOT" content="index, follow" /><meta name="msvalidate.01" content="C90FD08E2B78580B9B76A0554A160095" /><meta name="yandex-verification" content="914bfb8bd226480f" /> <link rel="Stylesheet" href="styl2.css"></head><header><br><center><h1>Witamy na stronie sklepu zoologicznego Art.Zoo Białystok ul. Sosabowskiego 2 sklep mieści się w budynku Tesco. </h1></center><right>Specjalizacja sklepu: akwarystyka</right></header><main><nav><br><br><br><center><a href="http://www.artzoo.bialystok.pl/"><img src="g869.png" alt="domek" title="strona główna" width="50" height="50"></a></center><br><br><br><center><a target="_blank" href="adres.html"><img src="g826.png" alt="telefon" title="kontakt ze sprzedawcą" width="50" height="50"></a></center><br><br><br><center><a target="_blank" href="https://www.google.com/maps/place/Genera%C5%82a+Stanis%C5%82awa+Sosabowskiego+2,+15-182+Bia%C5%82ystok/@53.145301,23.181233,17z/data=!3m1!4b1!4m5!3m4!1s0x471ffe9dfbe8176f:0x4f622e8bbcea47f0!8m2!3d53.1452978!4d23.1834217"><img src="g881.png" alt="lokalizacja" title="lokalizacja sklepu" width="50" height="50"></a></center><br><br><br><center><a target="_blank" href="https://www.google.com/maps/place/Genera%C5%82a+Stanis%C5%82awa+Sosabowskiego+2,+15-182+Bia%C5%82ystok/@53.1456215,23.1829824,3a,55.8y,187.12h,83.9t/data=!3m6!1e1!3m4!1sg62CI1Asimw48lXgt570Fw!2e0!7i13312!8i6656!4m5!3m4!1s0x471ffe9dfbe8176f:0x4f622e8bbcea47f0!8m2!3d53.1452978!4d23.1834217"><img src="g834.png" alt="podgląd" title="widok sklepu" width="50" height="50"></a></center><br><br><br><center><a href="galeria.html"><img src="g851.png" alt="aparat" title="galeria" width="50" height="50"></center><br><br><br></nav><article><br>M E N U: &nbsp;<a target="_blank" href="https://www.google.com/maps/place/Genera%C5%82a+Stanis%C5%82awa+Sosabowskiego+2,+15-182+Bia%C5%82ystok/@53.145301,23.181233,17z/data=!3m1!4b1!4m5!3m4!1s0x471ffe9dfbe8176f:0x4f622e8bbcea47f0!8m2!3d53.1452978!4d23.1834217"><input type="button" value="lokalizacja sklepu&hellip;" /></a>&nbsp;<a target="_blank" href="https://www.google.com/maps/place/Genera%C5%82a+Stanis%C5%82awa+Sosabowskiego+2,+15-182+Bia%C5%82ystok/@53.1456215,23.1829824,3a,55.8y,187.12h,83.9t/data=!3m6!1e1!3m4!1sg62CI1Asimw48lXgt570Fw!2e0!7i13312!8i6656!4m5!3m4!1s0x471ffe9dfbe8176f:0x4f622e8bbcea47f0!8m2!3d53.1452978!4d23.1834217"><input type="button" value="podgląd&hellip;" /></a>&nbsp;<a target="_blank" href="adres.html"><input type="button" value="kontakt ze sprzedawcą&hellip;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="art_zoo_napis.png" alt="art zoo " width="300" height="100" ><br>')
    for i in range(bbb):
        
        linie=(tekst.get(str(i)+".0",str(i+1)+".0")) + "<br>"
        plik.write(linie)
        
    plik.write('<br><scetion><img src="zdjecia/gdzikupisgupika.jpeg" alt="gdzie kupić gupika " width="60" height="60"><img src="zdjecia/gupik.jpeg" alt="gupik gdzie kupić ryby akwariowe białystok" width="60" height="60" ><img src="zdjecia/karma_dla_chomika.jpeg" alt="pokarm dla chomika świnki koszatniczki królika"width="60" height="60"><img src="zdjecia/karmay.jpeg" alt=" pokarmy dla ryb białystok"width="60" height="60"><img src="zdjecia/mieczyk.jpeg" alt="mieczyk ryba białystok " width="60" height="60"><img src="zdjecia/mieczyk_artzoo.jpeg" alt="mieczyk sklep zoologiczny " width="60" height="60"><img src="zdjecia/mieczyk-artzoo.jpeg" alt="mieczyki bialystok zoologiczny " width="60" height="60"><img src="zdjecia/mieczykryba.jpeg" alt="mieczyk - sklep akwarystyczny " width="60" height="60"><img src="zdjecia/mieczyk_ryba.jpeg" alt="gdzie kupic mieczyka "width="60" height="60"><img src="zdjecia/napowietrzanie.jpeg" alt="akcesoria do akwarium bialystok napowietrzacze " width="60" height="60"><br><img src="zdjecia/ozdoby_akwariowe.jpeg" alt="ozdoby do akwarium akcesoria ceramika "width="60" height="60"><img src="zdjecia/podlaska.jpeg" alt="podlaskie podlaskim " width="60" height="60"><img src="zdjecia/pokarm_dlaryb.jpeg" alt="pokarmy dla ryb akwariowych " width="60" height="60"><img src="zdjecia/preparaty_akwarystyczne.jpeg" alt="lekarstwa dla ryb uzdatniacze wody " width="60" height="60"><img src="zdjecia/ros-bialystok.jpeg" alt="rosliny w bialymstoku " width="60" height="60"><img src="zdjecia/roslina.jpeg" alt="roslina rośliny roslinki"width="60" height="60"><img src="zdjecia/roslina_artzoo.jpeg" alt="akwarystyka słodkowodna ryby do akwarium białystok " width="60" height="60"><img src="zdjecia/rosliny_art.jpeg" alt="art zoologiczne rośliny słodkowodne " width="60" height="60"><img src="zdjecia/ryba_welon.jpeg" alt="welon ryba akwariowa " width="60" height="60"><img src="zdjecia/ryby.jpeg" alt="ryba Art.Zoo Białystok "width="60" height="60"></section></article><aside><br><center> <br><b>C z y n n e</b><br><table> <tbody><tr><td>poniedziałek</td> <td>10:00 - 17:00</td> </tr> <tr> <td>wtorek</td><td>10:00 - 17:00</td> </tr> <tr> <td>środa</td> <td>10:00 - 17:00</td> </tr> <tr><td>czwartek</td>    <td>10:00 - 17:00</td> </tr> <tr> <td>piątek</td>    <td>10:00 - 17:00</td> </tr> <tr> <td>sobota</td>    <td>10:00 - 14:00</td> </tr> <tr> <td>niedziela</td>    <td>nieczynne</td> </tr> </tbody></table><form method="post" action="art_zoo.php"><div class="select-style"><select name="lista[]" size="3"  multiple="TRUE"><option value="ryby"> ryby </option><option value="rosliny"> rośliny</option><option value="zwierzeta_wodne">zwierzęta wodne</option></select></div><br><div><input class="input" type="submit" value="zobacz"></div></form><br><img src="zdjecia/sklep.jpeg" alt="akwarystyka" title="sklep zoologiczny ryby" width="200" height="200"><img src="zdjecia/mieczyk_artzoo.jpeg" alt="mieczyk" title="gdzie kupić mieczyka" width="200" height="200"></center><br><center><b>Akceptujemy karty płatnicze</b><br></center></aside></main><footer><center>ArtZoo 2019 Białystok ul.Sosabowskiego 2 ( budynek TESCO )</center></footer></html>')   
    plik.close()
    print("zamknięcie pliku")
    print("start wysyłania")
    ftp = FTP()
    
    ftp.set_debuglevel(2)
    ftp.connect('xxxxx', 21) 
    ftp.login('xxxxx','xxxxx')
    
    
    file = open("index.html","rb")                  # file to send
    ftp.storbinary("STOR index.html", file)          # send the file
    file.close()                                    # close file and FTP
    ftp.quit()
    print("zakończone wysyłanie")
    opis="transfer ok"
    info = Label(okno, fg = "green",text=opis)
    info.pack()
okno = tk.Tk()
print("To okno ma się otwierać wszystko działa prawidłowo")
przycisk = tk.Button(okno, text="wyślij", command = wysylanie)

tekst = tk.Text(okno)


tekst.pack()
przycisk.pack()

okno.mainloop()