#!/usr/bin/env python

import bottle
import random
import json
import os
from model import Uporabnik, Igra

imenik_s_podatki = 'uporabniki'
uporabniki = {}

if not os.path.isdir(imenik_s_podatki):
    os.mkdir(imenik_s_podatki)

@bottle.get('/')
def zacetna_stran():
    return bottle.template('index.html')

@bottle.post('/')
def zacetna_stran_post():
    st_vrstic = int(bottle.request.forms.getunicode('st_vrstic'))
    st_stolpcev = int(bottle.request.forms.getunicode('st_stolpcev'))
    global matrika
    global score
    global username
    score = 0
    username = bottle.request.forms.getunicode('uporabnisko_ime')
    matrika = [[random.randint(0, 1) for _ in range(st_vrstic)] for _ in range(st_stolpcev)]
    return bottle.template('gameplay.html', matrika = matrika, score = score)

@bottle.get('/gameplay/<row>/<col>/')
def gameplay_get(row, col):
    global matrika
    if matrika[int(row)][int(col)] == 0:
        global score
        score += 10
        matrika[int(row)][int(col)] = 'X'
        return bottle.template('gameplay.html', matrika = matrika, score = score)
    else:
        global username
        with open(imenik_s_podatki + '/' + username + '.json', 'w') as file:
            u = Uporabnik(username, score)
            json.dump(u.__dict__, file, indent = 4)
        return bottle.template('index.html', warning = '', score = score)

bottle.run(host='127.0.0.1', port = 80, debug = True, reloader = True)