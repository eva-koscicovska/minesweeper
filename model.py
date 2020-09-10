import json
import os

class Uporabnik:
    def __init__(self, uporabnisko_ime, score):
        self.uporabnisko_ime = uporabnisko_ime
        self.score = score

    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
        uporabnisko_ime = slovar_stanja['uporabnisko_ime']
        score = slovar_stanja['score']
        return cls(uporabnisko_ime, score)

    @classmethod
    def nalozi_vsi(cls, imenik_s_podatki):
        uporabniki = []
        if not os.path.isdir(imenik_s_podatki):
            os.mkdir(imenik_s_podatki)
        else:
            for ime_datoteke in os.listdir(imenik_s_podatki):
                uporabnik = cls.nalozi_stanje(os.path.join(imenik_s_podatki, ime_datoteke))
                uporabniki.append(uporabnik)
            uporabniki.sort(key = lambda x: x.score, reverse = True)
        return uporabniki

    def shrani_stanje(self, imenik_s_podatki):
        path = os.path.join(imenik_s_podatki, f'{self.uporabnisko_ime}.json')
        if os.path.isfile(path):
            with open(path, encoding = 'utf-8') as file:
                slovar_stanja = json.load(file)
                if self.score < slovar_stanja['score']:
                    self.score = slovar_stanja['score']
        with open(path, 'w') as file:
            json.dump(self.__dict__, file, ensure_ascii = False, indent = 4)

class Igra:
    def __init__(self, vrstice, stolpcev):
        self.vrstice = vrstice
        self.stolpcev = stolpcev

    @classmethod
    def okoli_stej(cls, matrika, row, col):
        okoli_stevec = 0

        try:
            if row - 1 > -1 and matrika[row - 1][col] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        try:
            if matrika[row + 1][col] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        try:
            if col - 1 > -1 and matrika[row][col - 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if matrika[row][col + 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if row - 1 > -1 and matrika[row - 1][col + 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if row - 1 > -1 and col - 1 > -1 and matrika[row - 1][col - 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if matrika[row + 1][col + 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        try:
            if col - 1 > -1 and matrika[row + 1][col - 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        matrika[row][col] = okoli_stevec