from freegames import floor
from turtle import *
import numpy as np


class Labirinto:
    def __init__(self, dim,tam_celula):
        self._dim = dim
        self._tam_celula = tam_celula

    def obter_vizinhos(lin, col):
        """ Retorna uma lista com os vizinhos (cima, baixo, esquerda, direita) da célula que são caminho.
            As coordenadas (lin, col) são da matriz. Por exemplo, na matriz a seguir:
            [[ 0  1  0 ]
             [ 1  1  0 ]
             [ 0  0  1 ]]
             Os vizinhos do elemento central (1,1) incluem o de cima (0,1) e o da
             esquerda (1,0). O vizinho de baixo (2,1) e o da direita (1,2) não são
             incluídos porque estão com valor 0. Nem os elementos da diagonal porque
             não entram na definição de vizinhança adotada aqui.
        """
        pass

    def ler_matriz_fixa(self):
        """ Retorna uma matriz fixa """
        return [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]


    def ler_matriz_aleatoria(dim):
        """ Retorna uma matriz quadrada na dimensão especificada com números
            aleatórios (0's e 1's)
            Dica: utilize numpy.random.randint()
        """
        return np.random.randint(2,size=(dim,dim))


    def criar_labirinto(self,p1=500, p2=500, p3=370, p4=0):
        """ Cria o gráfico do labirinto baseado nos valores da matriz """
        tracer(False)
        hideturtle()
        bgcolor('black')
        setup(p1, p2, p3, p4)

        # Para cada linha da matriz
        for lin in range(self._dim):
            # Para cada coluna da matriz
            for col in range(self._dim):
                # Testa se a coordenada da matriz (lin, col) é caminho (=1)
                if (matriz[lin][col] == 1):
                    # Em caso positivo, transforma em coordenada Turtle.
                    # Atenção: Numa coordenada Turtle (x,y), o eixo x refere-se à coluna e o eixo y à linha
                    # Numa coordenada da matriz (lin, col), o primeiro elemento é a linha e o segundo a coluna
                    x, y = self.em_coord_turtle(lin, col)
                    # Pinta a celula na posição (x,y) com a cor especificada
                    self.desenhar_celula(x, y, 'blue')

                    self.desenhar_pastilha(x, y, 'white')

    def desenhar_celula(self,x, y, cor):
        """ Dada uma coordenada (x, y) do Turtle, desenha um quadrado (célula) na posição """
        color(cor)
        up()
        goto(x,y)
        down()
        begin_fill()
        for _ in range(4):
            forward(self._tam_celula)
            left(90)
        end_fill()
        up()

    def chao_da_celula(self,x, y):
        """ Dadas coordenadas do Turtle (x,y), retorna as coordenadas do início de uma célula.
            Por exemplo, na celula da origem com tamanho 20, a coordenada Turtle (10,10)
            representa o meio da célula. A chamada de função 'chao_da_celula(10, 10)' retorna
            as coordenadas de início dessa célula (0,0)
            Dica: para entender, veja o exemplo da função: 'uso_do_floor()''
        """
        chao_x = int(floor(x, self._tam_celula))
        chao_y = int(floor(y, self._tam_celula))
        return chao_x, chao_y

    def em_coord_turtle(self,lin, col):
        """ Dados os índices da matriz (lin, col), retorna as coordenadas do Turtle correspondentes.
            Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
            a chamada de função 'em_coord_turtle(0,0)' deve retornar (-200,200) e a
            chamada de função 'em_coord_turtle(10,10)' deve retornar (0,0)
        """
        meio = self._dim // 2
        x = (col - meio) * self._tam_celula
        y = (meio - lin) * self._tam_celula
        return x, y

    def em_coord_matriz(self,x, y):
        """ Dada uma coordenada do Turtle (x,y), retorna os índices correspondentes da matriz
            Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
            a chamada de função 'em_coord_matriz(-200, 200)' deve retornar (0,0) e a
            chamada de função 'em_coord_matriz(0, 0)' deve retornar (10,10).
            Dica: utilize a função 'chao_da_celula(x, y)'
        """
        x, y = self.chao_da_celula(x, y)
        meio = self._dim // 2
        lin = int(meio - (y / self._tam_celula))
        col = int(meio + (x / self._tam_celula))
        return lin, col

    def cel_aleatoria(self):
        """ Retorna os índices de uma posição que contenha 1
            Por exemplo, na matriz a seguir:
            [[ 1  0  0 ]
             [ 0  1  0 ]
             [ 0  0  1 ]]
            Somente os elementos da diagonal principal [(0,0), (1,1), (2,2)]
            poderiam ser retornados
            Dica: utilize numpy.random.randint()
        """
        i, j = np.random.randint(self._dim, size=(2))
        while (not self.eh_caminho(i, j)):
            i, j = np.random.randint(self._dim, size=(2))
        return i, j

    def eh_caminho(self,lin, col):
        """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
            False caso contrário.
            Por exemplo, na matriz a seguir:
            [[ 1  0  0 ]
             [ 0  1  0 ]
             [ 0  0  1 ]]
            a chamada de função 'eh_caminho(0,0)' retorna True e
            a chamada de função 'eh_caminho(0,1)' retorna False
        """
        return matriz[lin][col] == 1

    def desenhar_pastilha(self,x, y, cor):
        """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
            para representar a pastilha
        """
        c = self._tam_celula // 2
        up()
        goto(x + c,y + c)
        down()
        dot(3, cor)


matriz = Labirinto.ler_matriz_aleatoria(20)

