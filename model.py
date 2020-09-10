import json
import os
import random

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
    def generiraj_matrika(self, st_vrstic, st_stolpcev):
        self.matrika = [[random.randint(-2, -1) for _ in range(st_vrstic)] for _ in range(st_stolpcev)]

        stevec = 0
        for row in self.matrika:
            for col in row:
                if col == -1:
                    stevec += 1
        self.stevec = stevec

        for row in self.matrika:
            for col in row:
                print(col)
            print('xD')

    def podaj_uporabnik(self, uporabnik):
        self.uporabnik = uporabnik

    def okoli_stej(self, row, col):
        okoli_stevec = 0

        try:
            if row - 1 > -1 and self.matrika[row - 1][col] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        try:
            if self.matrika[row + 1][col] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        try:
            if col - 1 > -1 and self.matrika[row][col - 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if self.matrika[row][col + 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if row - 1 > -1 and self.matrika[row - 1][col + 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if row - 1 > -1 and col - 1 > -1 and self.matrika[row - 1][col - 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass
        
        try:
            if self.matrika[row + 1][col + 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        try:
            if col - 1 > -1 and self.matrika[row + 1][col - 1] == -1:
                okoli_stevec += 1
        except IndexError as identifier:
            pass

        self.matrika[row][col] = okoli_stevec

    def povecaj_skor(self, stevilo):
        self.uporabnik.score += stevilo

    def zamenjaj_skor(self, score):
        self.uporabnik.score = score