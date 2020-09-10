#!/usr/bin/env python

import bottle
from model import Uporabnik, Igra

IMENIK_S_PODATKI = 'uporabniki'
MINA_SKOR = 10
ZMAGA_SKOR_VEČKRATNIK = 2
igra = Igra()

@bottle.get('/')
def zacetna_stran():
    return bottle.template('index.html', uporabniki = Uporabnik.nalozi_vsi(IMENIK_S_PODATKI))

@bottle.post('/')
def zacetna_stran_post():
    st_vrstic = int(bottle.request.forms.getunicode('st_vrstic'))
    st_stolpcev = int(bottle.request.forms.getunicode('st_stolpcev'))
    igra.generiraj_matrika(st_vrstic, st_stolpcev)
    igra.podaj_uporabnik(Uporabnik(bottle.request.forms.getunicode('uporabnisko_ime'), 0))   
    return bottle.template('gameplay.html', matrika = igra.matrika, score = igra.uporabnik.score, stevec = igra.stevec)

@bottle.get('/gameplay/<row>/<col>/')
def gameplay_get(row, col):
    matrika = igra.matrika
    username = igra.uporabnik.uporabnisko_ime
    score = igra.uporabnik.score
    if matrika[int(row)][int(col)] == -2:
        igra.povecaj_skor(MINA_SKOR)
        score = igra.uporabnik.score
        igra.okoli_stej(int(row), int(col))
        for row in igra.matrika:
            for col in row:
                if col == -2:
                    return bottle.template('gameplay.html', matrika = matrika, score = score, stevec = igra.stevec)
        score *= ZMAGA_SKOR_VEČKRATNIK
        igra.zamenjaj_skor(score)
        igra.uporabnik.shrani_stanje(IMENIK_S_PODATKI)
        return bottle.template('index.html', warning = 'You won!', score = score)
    else:
        igra.uporabnik.shrani_stanje(IMENIK_S_PODATKI)
        return bottle.template('index.html', warning = 'You lost!', score = score)

@bottle.get('/pomoc')
def pomoc():
    return bottle.template('pomoc.html')

bottle.run(host = '127.0.0.1', port = 80, debug = True, reloader = True)