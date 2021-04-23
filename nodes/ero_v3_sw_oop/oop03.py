#!/usr/bin/python
# -*- coding: utf-8 -*-
##oop03_statVar.py

import sys

class Schokofigur:
    #statische Variable fuer alle Objekte der Klasse gemeinsam
    schoko_gesamt = 0
    def __init__(self,name, gewicht): #Konstruktor
        # Name der Klasse. Name der stat. Var
        Schokofigur.schoko_gesamt += gewicht
        
        # Normale Variable
        self._bez = name
    def getBez(self):
        return self._bez
        
    def __str__ (self): #String-Ausgabe überladen
        myStr = (self._bez + " ist " + str(Schokofigur.schoko_gesamt) +" g schwer")
        return myStr

if __name__ == '__main__':
    objekt1 = Schokofigur('Weihnachtsmann', 200)
    objekt2 = Schokofigur("Osterei",50)
    print(objekt2)    
    print(objekt1.getBez())
    print("Geamstgewicht Schokolade: " + str(Schokofigur.schoko_gesamt))
