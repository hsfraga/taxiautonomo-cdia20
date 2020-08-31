from turtle import *

class Agente:
    def __init__(self,tam_agente, tam_celula):
        self._tam_celula = tam_celula
        self._tam_agente = tam_agente

    def desenhar_agente(self,x,y,cor):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar o agente (i.e., pacman, fantasmas)
        """
        c = self._tam_celula // 2
        up()
        goto(x + c,y + c)
        down()
        dot(self._tam_agente, cor)

