import matplotlib.pyplot as plt
import math
from config import CABOS

def plotar_geometria(cabos_dict=CABOS):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Listas para definir limites do gráfico
    alturas = []
    
    for nome, dados in cabos_dict.items():
        x = dados['x']
        y = dados['y']
        tipo = dados['tipo']
        alturas.append(y)
        
        # Cor diferente para para-raio vs fase
        cor = 'red' if tipo == 'para-raio' else 'blue'
        marcador = '^' if tipo == 'para-raio' else 'o'
        
        ax.plot(x, y, marker=marcador, markersize=12, color=cor, label=tipo)
        
        # Anotação
        ax.annotate(nome, xy=(x, y), xytext=(5, 5), textcoords='offset points',
                    fontsize=10, fontweight='bold')

        # Linhas de projeção
        ax.plot([x, x], [0, y], 'k--', linewidth=0.5, alpha=0.5) # Vertical
        ax.plot([0, x], [y, y], 'k--', linewidth=0.5, alpha=0.5) # Horizontal

    # Ajustes estéticos (sem duplicar labels na legenda)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())

    # Limites
    margem = 5
    max_h = max(alturas)
    ax.set_ylim(0, max_h + margem)
    ax.set_xlim(-15, 15) # Ajustável conforme geometria
    
    ax.set_xlabel('Posição Horizontal (m)')
    ax.set_ylabel('Altura (m)')
    ax.set_title('Geometria da Torre')
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Eixos centrais
    ax.axvline(x=0, color='black', linewidth=1)
    ax.axhline(y=0, color='black', linewidth=1)

    plt.tight_layout()
    return fig

if __name__ == "__main__":
    plotar_geometria()
    plt.show()