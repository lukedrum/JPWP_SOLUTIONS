#ok
import pygame
from przyciski import Przycisk,PrzyciskTekstowy
import time as t


class PasekDolny:


    def __init__(self, x, y, gra):
        self.x = x
        self.y = y
        self.SZEROKOSC = 720
        self.WYSOKOSC = 100
        self.OBRAMOWANIE = 5
        self.gra = gra
        self.czysc_button = PrzyciskTekstowy(810, 490 ,110 ,55, (128,128,128), "Czyść")
        self.gumka_button = PrzyciskTekstowy(925,490,110, 55, (128,128,128), "Gumka")
        self.flaga = True



    def rysuj(self, win):
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.SZEROKOSC, self.WYSOKOSC), self.OBRAMOWANIE)
        self.czysc_button.rysuj(win)
        self.gumka_button.rysuj(win)



    def obsluga_przyciskow(self):
        
        mouse = pygame.mouse.get_pos()

        if self.czysc_button.klikniecie(*mouse):
            self.gra.tablica.czyszczenie()
            self.gra.connection.send({10:[]})


        ###############################################

        if self.gumka_button.klikniecie(*mouse):

        ### Napisz kod do zadania nr 2

            if self.flaga == True:
                self.gra.kolor_rysowania = (255,255,255)  # czarny
                self.flaga = False
                t.sleep(0.1)
            else:
                self.gra.draw_kolor_rysowania = (0,0,0)  # biały
                self.flaga = True
                t.sleep(0.3)

        ################################################

