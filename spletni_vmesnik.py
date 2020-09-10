#!/usr/bin/env python

import bottle
import random
import json
import os
import hashlib
from model import Uporabnik, Igra

IMENIK_S_PODATKI = 'uporabniki'

@bottle.get('/')
def zacetna_stran():
    return bottle.template('index.html', uporabniki = Uporabnik.nalozi_vsi(IMENIK_S_PODATKI))

@bottle.post('/')
def zacetna_stran_post():
    st_vrstic = int(bottle.request.forms.getunicode('st_vrstic'))
    st_stolpcev = int(bottle.request.forms.getunicode('st_stolpcev'))
    global matrika
    global score
    global username
    global stevec
    stevec = 0
    score = 0
    username = bottle.request.forms.getunicode('uporabnisko_ime')
    matrika = [[random.randint(-2, -1) for _ in range(st_vrstic)] for _ in range(st_stolpcev)]
    
    for row in matrika:
        for col in row:
            print(col)
        print('xD')

    for row in matrika:
        for col in row:
            if col == -1:
                stevec += 1
    return bottle.template('gameplay.html', matrika = matrika, score = score, stevec = stevec)

@bottle.get('/gameplay/<row>/<col>/')
def gameplay_get(row, col):
    global matrika
    global username
    if matrika[int(row)][int(col)] == -2:
        global score
        score += 10
        Igra.okoli_stej(matrika, int(row), int(col))
        for row in matrika:
            for col in row:
                if col == -2:
                    return bottle.template('gameplay.html', matrika = matrika, score = score, stevec = stevec)
        score *= 2
        Uporabnik(username, score).shrani_stanje(IMENIK_S_PODATKI)
        return bottle.template('index.html', warning = 'You won!', score = score)
    else:
        Uporabnik(username, score).shrani_stanje(IMENIK_S_PODATKI)
        return bottle.template('index.html', warning = 'You lost!', score = score)

@bottle.get('/pomoc')
def pomoc():
    return bottle.template('pomoc.html')

bottle.run(host = '127.0.0.1', port = 80, debug = True, reloader = True)