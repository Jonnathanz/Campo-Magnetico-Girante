import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

'''
    Autor:      Jonnathan Alves Ramos
    Disciplina: Máquinas Elétricas 1

    Descrição:  Simulação do campo magnético girante de um motor de indução com
                alimentação monofásica.
'''

def main():
    figure, axes = plt.subplots(figsize=(8,8))                      # Define o tamanho da figura em 5 polegadas em X e Y

    circle = plt.Circle(
                            (0,0),                                  # Centro do círculo
                            1.5,                                    # Raio do círculo
                            fill  =False,                           # Retira o preenchimento do círculo
                            color ="black"       
                        )
    axes.add_artist(circle)                                         # Adiciona o círculo na figura
    vector = axes.quiver(
                            0, 0, 0, 0,                             # X(inicial), Y(inicial), X(final), Y(final)
                            angles      ="xy",        
                            scale_units ="xy",                       # Escala em relação aos eixos X e Y
                            scale       =1,                          # Escala = 1
                            color       ='red',
                            label       = 'Campo magnético da Fase A'
                        )
    plt.xlim(-2,2)                                                  # Configura os intervalos no eixo X
    plt.ylim(-2,2)                                                  # Configura os intervalos no eixo Y
    plt.axis('off')                                                 # Não mostra os eixos na figura
    plt.title('Campo girante com alimentação monofásica')

    def update(t):
        t *= 0.05                                                   # Passo do tempo t para 0.05, variando de 0 até 6.25 conforme os frames
        ### Equações da FEM:
        # Fm = 1, w = 1
        Fa = np.array([np.cos(t), 0])
        ###
        U = Fa[0]                                                   # Atualiza o X(final) conforme a equação
        V = Fa[1]                                                   # Atualiza o Y(final) conforme a equaçãos

        vector.set_UVC(U, V)                                        # Atualiza o X(final) e Y(final)

        return vector

    anim = FuncAnimation(
                            figure,
                            update,                                 # Função de callback para cada atualização
                            interval=50,                            # interval: intervalo entre os frames em milissegundos
                            frames=126,                             # Quantidade de frames por repetição
                            blit=False                              # Não utiliza a lista de retornos para atualizar
                         )
    plt.legend()
    anim.save('Lista_03_a.gif', dpi=80, writer='imagemagick')
    plt.show()
    

if __name__ == '__main__':
    main()
