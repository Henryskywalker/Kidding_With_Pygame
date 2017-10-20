#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

width  = 900
height = 400

#Classe da nave
class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("nave.png")
        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = width / 2
        self.rect.centery = height - 50
        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()
    
    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()
    
    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 900:
                self.rect.right = 900

  

    def disparar(self, x, y):
        minhaBala = Bala(x,y)
        self.listaDisparo.append(minhaBala)

    def colocar(self, superficie):
        superficie.blit(self.ImagemNave,(self.rect))
#Classe da bala
class Bala(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load("balaa.png")
        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 6
        self.rect.top = pos_x
        self.rect.left = pos_x
    
    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala

    def colocar(self, superficie):
        superficie.blit(self.ImagemBala, (self.rect))
#Classe do Inimigo
class Inimigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.Alien = pygame.image.load("Alien.png")
        self.Alien2 = pygame.image.load("Alien2.png")

        self.listaImagens = [self.Alien, self.Alien2]
        self.posImagem    = 0
        self.imagemAlien  = self.listaImagens[self.posImagem]

        #self.rect = self.imagemAlien.get_rect()



        self.rect = self.Alien.get_rect()
        self.listaDisparo = []
        self.velocidade = 20
        self.rect.top = pos_x
        self.rect.left = pos_x
    
        self.configTempo = 1

    def comportamento(self, tempo):
        if self.configTempo == tempo:
            print("Joined")
            self.posImagem += 1
            self.configTempo += 1
            if self.posImagem > len(self.listaImagens) - 1:
                self.posImagem = 0

    def colocar(self, superficie):
        self.imagemAlien = self.listaImagens[self.posImagem]
        superficie.blit(self.Alien, (self.rect))

#Funcao onde havera a execucao
def invasaoEspaco():
    pygame.init()
    tela = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Invasão do Espaço")

    jogador = naveEspacial()
    ImagemFundo = pygame.image.load("background.png")
    jogando = True

    inimigo = Inimigo(100,100)

    balaProjetil = Bala(width/2, height-90)

    relogio = pygame.time.Clock()

    while True:
        relogio.tick(60)
        tempo = int(pygame.time.get_ticks()/1000)
        #jogador.movimento()
        balaProjetil.trajetoria()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    jogador.movimentoEsquerda()
                elif event.key == pygame.K_RIGHT:
                    jogador.movimentoDireita()
                elif event.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparar(x,y)

        tela.blit(ImagemFundo, (0,0))
        balaProjetil.colocar(tela)
        jogador.colocar(tela)
        inimigo.colocar(tela)
        inimigo.comportamento(tempo)
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
        pygame.display.update()

invasaoEspaco() 