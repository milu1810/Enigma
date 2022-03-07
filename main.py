import re

def menu():
    f1 = open(r'C:\Users\Lucas\Desktop\Nouveau dossier\nomFichier.txt', 'r', encoding='utf8')
    f2 = open(r'C:\Users\Lucas\Desktop\Nouveau dossier\nomFichier.txt', 'a', encoding='utf8')
    if (len(f1.read()) < 255):
        f2.write(input('ecrire'))
    else:
        print("Tu parles trop")
        f2.close()
    LectureMessage()
    SauvegardeMessage()
    choixDuRotor()
    f1.close()
    f2.close()


def LectureMessage(f3=open(r'C:\Users\Lucas\Desktop\Nouveau dossier\nomFichier.txt', 'r', encoding='utf8'), mess = str):
    global texte
    mess = f3.readline()
    mess = mess.replace(" ", "")
    mess = re.sub(u"[àáâãäå]",'a',mess)
    mess = re.sub(u"[èéêë]", 'e', mess)
    mess = re.sub(u"[ìíîï]", 'i', mess)
    mess = re.sub(u"[òóôõö]", 'o', mess)
    mess = re.sub(u"[ùúûü]", 'u', mess)
    mess = re.sub(u"[ýÿ]", 'y', mess)
    mess = mess.upper()
    texte = mess
def SauvegardeMessage(f4=open(r'C:\Users\Lucas\Desktop\Nouveau dossier\nomFichier2.txt', 'a', encoding='utf8')):
    f4.write(texte)
    f4.close()

def choixDuRotor():
    reponseEnigma = texte
    rotor = {
        "alphabet" : ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"],
        "RA": ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I",
          "B", "R", "C", "J"],
        "RB" : ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y",
          "F", "V", "O", "E"],
        "RC" : ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M",
          "U", "S", "Q", "O"],
        "RD" : ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G", "K", "D",
          "C", "M", "W", "B"],
        "RE" : ["R", "D", "O", "B", "J", "N", "T", "K", "V", "E", "H", "M", "L", "F", "C", "W", "Z", "A", "X", "G", "Y", "I",
          "P", "S", "U", "Q"],
        "RFA" : ["Y", "R", "U", "H", "Q", "S", "L", "D", "P", "X", "N", "G", "O", "K", "M", "I", "E", "B", "F", "Z", "C", "W",
           "V", "J", "A", "T"],
        "RFB" : ["R", "D", "O", "B", "J", "N", "T", "K", "V", "E", "H", "M", "L", "F", "C", "W", "Z", "A", "X", "G", "Y", "I",
           "P", "S", "U", "Q"]
    }
    choix = int(input("Veuillez bien choisir votre nombre de 1 à 5"))
    while(choix >= 5 or choix < 0):
        choix = int(input("veuillez bien prendre un nombre entre 1 et 5"))
    if choix == 1:
        for a in reponseEnigma:
            reponseEnigma = ""
            reponseEnigma += a.join(rotor["RA"])
    elif choix == 2:
        for a in reponseEnigma:
            reponseEnigma = ""
            reponseEnigma += a.join(rotor["RB"])

    elif choix == 3:
        for a in reponseEnigma:
            reponseEnigma = ""
            reponseEnigma += a.join(rotor["RC"])
    elif choix == 4:
        for a in reponseEnigma:
            reponseEnigma = ""
            reponseEnigma += a.join(rotor["RD"])

    elif choix == 5:
        for a in reponseEnigma:
            reponseEnigma = ""
            reponseEnigma += a.join(rotor["RE"])

    print(reponseEnigma)
    for b in reponseEnigma:
        reponseEnigma=""
        reponseEnigma+=b.join(rotor["RFA"])
    for b in reponseEnigma:
        reponseEnigma=""
        reponseEnigma+=b.join(rotor["RFB"])
    print(reponseEnigma)
menu()
