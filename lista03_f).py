import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation

'''
    Autor:      Jonnathan Alves Ramos
    Disciplina: Máquinas Elétricas 1

    Descrição:  Simulação do campo magnético girante de um motor de indução com
                alimentação trifásica e valores de corretes desiguais

                • Fa = 1,4  pu
                • Fb = 0,41 pu
                • Fc = 0,93 pu

'''

def main():
    figure, axes = plt.subplots(figsize=(8,8))                        # Define o tamanho da figura em 5 polegadas em X e Y
    circle = plt.Circle(
                            (0,-0.5),                                 # Centro do círculo
                            1.5,                                      # Raio do círculo
                            fill  = False,                            # Retira o preenchimento do círculo
                            color ="black"       
                        )
    axes.add_artist(circle)                                            # Adiciona o círculo na figura
    vector = axes.quiver(
                            0, -0.5, 0, 0,                             # X(inicial), Y(inicial), X(final), Y(final)
                            angles       = "xy",        
                            scale_units  = "xy",                       # Escala em relação aos eixos X e Y
                            scale        = 1,                          # Escala = 1
                            color        = 'red',
                            label        = 'Campo magnético Resultante'
                        )
    vectorA = axes.quiver(
                            0, -0.5, 0, 0,                             # X(inicial), Y(inicial), X(final), Y(final)
                            angles      = "xy",        
                            scale_units = "xy",                        # Escala em relação aos eixos X e Y
                            scale       = 1,                           # Escala = 1
                            color       = 'black',
                            label       = 'Campo magnético da Fase A'
                        )
    vectorB = axes.quiver(
                            0, -0.5, 0, 0,                             # X(inicial), Y(inicial), X(final), Y(final)
                            angles      = "xy",        
                            scale_units = "xy",                        # Escala em relação aos eixos X e Y
                            scale       = 1,                           # Escala = 1
                            color       = 'green',
                            label       = 'Campo magnético da Fase B'
                        )
    vectorC = axes.quiver(
                            0, -0.5, 0, 0,                             # X(inicial), Y(inicial), X(final), Y(final)
                            angles      = "xy",        
                            scale_units = "xy",                        # Escala em relação aos eixos X e Y
                            scale       = 1,                           # Escala = 1
                            color       = 'brown',
                            label       = 'Campo magnético da Fase C'
                        )

    plt.xlim(-2,2)                                                  # Configura os intervalos no eixo X
    plt.ylim(-2,2)                                                  # Configura os intervalos no eixo Y
    plt.axis('off')                                                 # Não mostra os eixos na figura
    plt.title('Campo girante com alimentação trifásica com correntes de valores diferentes')

    def update(t):
        t *= 0.05                                                   # Passo do tempo t para 0.05, variando de 0 até 6.25 conforme os frames

        ### Equações da FEM Trifásico:
        # Fm = 1, w = 1
        # Ia = 1.4*Im, Ib = 0.41*Im, Ic = 0.93
        Fa = 1.4*np.array([np.cos(t), 0])
        Fb = 0.41*np.cos(t - 2*np.pi/3)*np.array([np.cos(-2*np.pi/3), np.sin(-2*np.pi/3)])
        Fc = 0.93*np.cos(t + 2*np.pi/3)*np.array([np.cos(2*np.pi/3), np.sin(2*np.pi/3)])
        
        Ft = Fa + Fb + Fc
        ###
        
        U = Ft[0]                                                   # Atualiza o X(final) conforme a equação
        V = Ft[1]                                                   # Atualiza o Y(final) conforme a equaçãos

        vector.set_UVC(U, V)                                        # Atualiza o X(final) e Y(final)
        vectorA.set_UVC(Fa[0], Fa[1])
        vectorB.set_UVC(Fb[0], Fb[1])
        vectorC.set_UVC(Fc[0], Fc[1])
        
        return vector

    anim = FuncAnimation(
                            figure,
                            update,                                 # Função de callback para cada atualização
                            interval=50,                            # interval: intervalo entre os frames em milissegundos
                            frames=126,                             # Quantidade de frames por repetição
                            blit=False                              # Não utiliza a lista de retornos para atualizar
                         )
    plt.legend()
    anim.save('Lista_03_f.gif', dpi=80, writer='imagemagick')
    plt.show()

if __name__ == '__main__':
    main()
