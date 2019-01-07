# -------------------------------IMPORT-------------------------------
import urllib.request
import urllib.request
import os
import os.path
from tkinter.filedialog import askopenfilename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import ttk
from tkinter import *




# --------------------------------CHEMIN------------------------------

path = 'C:\Documents\email'
if not os.path.exists('C:\Documents'):
    os.makedirs('C:\Documents')
if not os.path.exists('C:\Documents\email'):
    os.makedirs('C:\Documents\email')


# ---------------------------Fonctionnalitées-------------------------


def test_mail(ch):
    motif = r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)"
    a = re.findall(motif, ch.strip())
    if len(a) > 0:
        adr = ''.join(a[0]).strip()
    else:
        adr = ''
    # vérification de syntaxe de l'adresse mail extraite
    if adr == '':
        return False
    else:
        motif = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
        return re.match(motif, adr) != None


def verif_mail(fichier):  # on parcour chaque ligne , si vrai alors on supp la ligne
    my_list = [line.rstrip('\n') for line in open(os.path.join(path, fichier))]
    with open(os.path.join(path, fichier), 'w') as f:
        for item in my_list:
            if test_mail(item) == True:
                f.write("%s\n" % item)


def url_test(url):  # site dispo ou non"
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'

    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False  ##inclu l'erreur 404


def syntaxe_url(URL):  # verifie la syntaxe
    long = len(URL)
    test = (URL[0:7])
    test2 = (URL[long - 4:long])
    test3 = (URL[long - 3:long])
    if test == 'http://' and test2 == '.com':
        return True
    elif test == 'https:/' and test2 == '.com':
        return True
    else:
        return False


def lect(nom):
    with open(nom, 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    carnet = [line for line in lines]
    return carnet


def lecture(nom):
    tmp = ""
    with open(os.path.join(path, nom), 'r') as f:
        tmp = f.read()
        f.close()
    return tmp


def importer(source, destination):
    fs = open(source, 'r')
    fd = open(destination, 'a')
    txt = fs.readline()
    # fd.write('\n')
    while txt:
        fd.write(txt)
        txt = fs.readline()
    fs.close()
    fd.close()


def ecriture(fichier, my_list):
    print(fichier)
    with open(fichier, 'a') as f:
        for item in my_list:
            f.write("%s\n" % item)


def SuppDouble(fichier):
    my_list = [line.rstrip('\n') for line in open(os.path.join(path, fichier))]
    my_list = set(my_list)  # tri la liste
    with open(os.path.join(path, fichier), 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)


def crawler(url, fichier):
    Page_Web = str(urllib.request.urlopen(url).read())
    pos = Page_Web.find("mailto:")
    maListe = []
    while pos != -1:
        Page_Web = Page_Web[pos:]
        pos = Page_Web.find('"')
        mail = Page_Web[0:pos]
        maListe.append(mail[7:pos])
        Page_Web = Page_Web[pos:]
        pos = Page_Web.find("mailto:")
    ecriture(fichier, maListe)


def mail(froma, sento, objet, mess):  # envoie un mail dest;obj;mess
    msg = MIMEMultipart()
    fromaddr = froma
    toaddr = sento
    obj = objet
    mes = mess
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = objet
    message = mes
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('florian.chevillard@edu.itescia.fr', 'chevillard.florian@outlook.com')
    mailserver.sendmail(fromaddr, sento, msg.as_string())
    mailserver.quit()


def callbackFunc(event):
    print("New Element Selected")


def Opentxt(filepath):
    name = askopenfilename(initialdir="C:/Documents/email",
                           filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    importer(name, filepath)


def mailiste(ex, ob, mess, fichier):
    my_list = [line.rstrip('\n') for line in open(os.path.join(path, fichier))]
    for item in my_list:
        mail(ex, item, ob, mess)


def crawler(url, path):
    listeR = []
    data = str(urllib.request.urlopen(url).read())
    pos = data.find("mailto:")
    maListe = []
    while pos != -1:
        data = data[pos:]
        pos = data.find('"')
        mail = data[0:pos]
        listeR.append(mail[7:pos])
        data = data[pos:]
        pos = data.find("mailto:")
        R = []  # adresses valides
        E = []  # adresses invalides
        reExt = re.compile(r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)")
        reVerif = re.compile(
            r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[ a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,3})$")
        print(reExt)
        print(reVerif)
    for ch in listeR:

        a = reExt.findall(ch.strip())
        if len(a) > 0:
            adr = ''.join(a[0]).strip()
        else:
            adr = ''
        if adr == '':
            E.append(ch)
        else:
            if reVerif.match(adr) != None:
                R.append(ch)
            else:
                E.append(ch)
                print(E)
                print(R)
    with open(os.path.join(path), 'a') as g:
        for i in R:
            g.write(i + '\n')
    g.close()


def aff():
    chemin = str(entree.get())
    fichier = str(entree.get() + ".txt")
    var1 = os.path.isfile('C:\Documents\email' + "\\" + chemin + ".txt")
    che = str('C:\Documents\email' + "\\" + chemin + ".txt")
    if (var1 == True):  # si le fichier existe on ouvre la nouvelle fonction avec le fichier sinon on le crée
        fenetre.destroy()
        page2(che, fichier)
    else:
        fichier = open(che, "x")
        fenetre.destroy()
        page2(che, fichier)



#----------------------------DESIGN-------------------------------------

# ---------------------------------IHM----------------------------------

# Page 1
fenetre = Tk('intro')
fenetre.title('page 1')
fenetre.geometry('250x100+50+50')
label = Label(fenetre, text="Nom de du fichier txt").grid(row=0, column=1)
Button(fenetre, text="OK", command=aff).grid(row=1, column=2)
entree = Entry(fenetre)
entree.grid(row=1, column=1)


def page2(filepath, fichier):
    two = Tk('liste page 2')
    two.title('page 2')
    two.geometry('300x300+100+100')
    liste = lect(filepath)
    fi2 = str('C:\Documents\email' + "\\""fichier.txt")
    name = StringVar(two)

    labelTop = tk.Label(two, text="Boite de mail")
    labelTop.grid(column=0, row=0)
    combo = ttk.Combobox(two, width=30, values=liste).grid(row=1, column=0)
    Button(two, text="retirer les  Doublons",
           command=lambda: [SuppDouble(fichier), page2(filepath, fichier), two.destroy()]).grid(row=2, column=0)
    Button(two, text="importer un txt ",
           command=lambda: [Opentxt(filepath), page2(filepath, fichier), two.destroy()]).grid(row=3, column=0)
    entr = Entry(two)
    entr.grid(row=4, column=1)
    Button(two, text="OK crawler :",
           command=lambda: [crawler(str(entr.get()), path), page2(filepath, fichier), two.destroy()]).grid(row=4,column=0)
    Button(two, text="Test des mails",
           command=lambda: [verif_mail(fichier), page2(filepath, fichier), two.destroy()]).grid(row=5, column=0)

    LabFin = Label(two, text="Une fois valider cliquer sur GO! pour lancer les mails")

    Button(two, text="GO!", command=lambda: [page3(filepath, fichier), two.destroy()]).grid(row=7, column=1)


def page3(filepath, fichier):
    three = Tk('message')
    three.title('page3')
    three.geometry('300x300+100+100')
    LabelExp = tk.Label(three, text="exp").grid(row=1, column=1)
    Exp = Entry(three, width=30)
    Exp.grid(row=2, column=1)
    LabelObj = tk.Label(three, text="Obj").grid(row=4, column=1)
    Obj = Entry(three, width=30)
    Obj.grid(row=5, column=1)
    LabelMsg = tk.Label(three, text="msg", ).grid(row=8, column=1)
    Msg = Entry(three, width=50)
    Msg.grid(row=9, column=1)
    Button(three, text="OK",
           command=lambda: [page4(str(Exp.get()), str(Obj.get()), str(Msg.get()), fichier), three.destroy()]).grid(
        row=10, column=1)


def page4(expediteur, objet, message, fichier):
    four = Tk('email send')
    four.title('page4')
    LabelTest = tk.Label(four, text="Email test").grid(row=1, column=1)
    Test = Entry(four)
    Test.grid(row=1, column=2)
    print(expediteur)
    b = Button(four, text="Test", command=lambda: [mail(expediteur, str(Test.get()), objet, message)])
    b.grid(row=2, column=2)
    b2 = Button(four, text="go mail", command=lambda: [mailiste(expediteur, objet, message, fichier)])
    b2.grid(row=3, column=2)




fenetre.mainloop()
