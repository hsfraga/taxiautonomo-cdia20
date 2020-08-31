from agente import *
from labirinto import *


class Pacman:

    def main():

        dimensao_da_matriz = 20
        tam_celula = 20

        # Cria o labirinto
        lab = Labirinto(dimensao_da_matriz, tam_celula)
        lab.criar_labirinto()

        # Cria o agente
        tam_agente = 20
        agente = Agente(tam_agente, tam_celula)

        # Obtém as coordenadas de onde inserir o agente e desenha na tela
        lin, col = lab.cel_aleatoria()
        x, y = lab.em_coord_turtle(lin, col)
        agente.desenhar_agente(x, y, 'yellow')

        # Atualiza o turtle e finaliza
        update()
        done()

    main()

