#!/usr/bin/env python

import bottle
import random
from model import Uporabnik, Igra


@bottle.get('/')
def zacetna_stran():
    return bottle.template('index.html')

@bottle.post('/')
def zacetna_stran_post():
    st_vrstic = int(bottle.request.forms.getunicode('st_vrstic'))
    st_stolpcev = int(bottle.request.forms.getunicode('st_stolpcev'))
    matrika = [[random.randint(0, 1) for _ in range(st_vrstic)] for _ in range(st_stolpcev)]
    return bottle.template('gameplay.html', matrika = matrika)

@bottle.get('/gameplay/0/0/')
def gameplay_post():
    print(matrika)
    return bottle.template('gameplay.html', matrika = matrika)

bottle.run(debug = True, reloader = True)