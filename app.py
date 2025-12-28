import streamlit as st
import numpy as np
import pandas as pd
from config import CABOS, FREQUENCIA, RESISTIVIDADE_SOLO
from calculo_de_parametros import calcular_matrizes
from mostrar_cabos import plotar_geometria
import copy

st.set_page_config(page_title="Redesigned Funicular - Parâmetros LT", layout="wide")

st.title("⚡ Análise de Parâmetros de Linhas de Transmissão")
st.markdown("""
Esta aplicação calcula os parâmetros elétricos (Indutância e Capacitância) de uma linha de transmissão
baseada na geometria da torre e nas características do solo.
""")

# --- Sidebar: Configurações Globais ---
st.sidebar.header("⚙️ Parâmetros do Sistema")
freq = st.sidebar.number_input("Frequência (Hz)", value=FREQUENCIA, step=10)
ro_solo = st.sidebar.number_input("Resistividade do Solo (Ω.m)", value=RESISTIVIDADE_SOLO, step=50)

# --- Sidebar: Configuração da Geometria ---
st.sidebar.subheader("📐 Geometria da Torre")
st.sidebar.info("Ajuste as coordenadas (x, y) dos cabos.")

# Criar cópia editável dos cabos
cabos_editaveis = copy.deepcopy(CABOS)

# Gerar inputs dinâmicos para cada cabo
for nome, dados in cabos_editaveis.items():
    with st.sidebar.expander(f"Cabo {nome} ({dados['tipo']})", expanded=False):
        col1, col2 = st.columns(2)
        cabos_editaveis[nome]['x'] = col1.number_input(f"X {nome} (m)", value=float(dados['x']), key=f"x_{nome}")
        cabos_editaveis[nome]['y'] = col2.number_input(f"Y {nome} (m)", value=float(dados['y']), key=f"y_{nome}")

# --- Corpo Principal ---

col_grafico, col_teoria = st.columns([1.2, 1])

with col_grafico:
    st.subheader("Visualização da Torre")
    fig = plotar_geometria(cabos_editaveis)
    st.pyplot(fig)

with col_teoria:
    st.subheader("📚 Teoria Aplicada")
    st.markdown(r"""
    **1. Indutância (Método de Carson):**
    A indutância mútua entre dois condutores $i$ e $j$ considerando o retorno pelo solo é dada por:
    
    $$
    L_{ij} = 2 \cdot 10^{-7} \ln\left(\frac{D_e}{D_{ij}}\right) \quad [H/m]
    $$
    
    Onde $D_e$ é a profundidade equivalente de retorno de Carson:
    $$
    D_e = 658.37 \sqrt{\frac{\rho}{f}}
    $$
    """)
    
    st.metric(label="Profundidade de Carson (De)", value=f"{658.37 * np.sqrt(ro_solo/freq):.2f} m")

# --- Resultados ---
st.markdown("---")
st.header("🧮 Resultados Calculados")

if st.button("Recalcular Parâmetros", type="primary"):
    nomes, L_mat, C_mat = calcular_matrizes(cabos_editaveis, freq, ro_solo)
    
    tab1, tab2 = st.tabs(["Matriz de Indutância [L]", "Matriz de Capacitância [C]"])
    
    with tab1:
        st.markdown("**Matriz Primitive de Indutância ($\mu H/km$)**")
        # Converter para uH/km para facilitar leitura (H/m * 1e6 * 1000 = errado. H/m * 1e6 = uH/m. Vamos usar mH/km ou Ohm/km)
        # Vamos usar o padrão de engenharia: Ohms/km (Reatância) ou H/km.
        # O script original printava L*1e6 (micro Henries / metro). = mili Henries / km.
        
        df_l = pd.DataFrame(L_mat * 1e6, index=nomes, columns=nomes)
        st.dataframe(df_l.style.background_gradient(cmap="Blues").format("{:.4f}"))
        st.caption("Valores em $\mu H/m$ (micro-Henry por metro).")
        
        # Calcular Reatância Indutiva (XL = 2*pi*f*L) ohms/km
        # L (H/m) * 1000 = H/km
        XL_mat = 2 * np.pi * freq * (L_mat * 1000)
        st.markdown("**Matriz de Reatância Indutiva ($\Omega/km$)**")
        st.dataframe(pd.DataFrame(XL_mat, index=nomes, columns=nomes).style.format("{:.4f}"))

    with tab2:
        st.markdown("**Matriz de Capacitância ($pF/m$)**")
        df_c = pd.DataFrame(C_mat * 1e12, index=nomes, columns=nomes)
        st.dataframe(df_c.style.background_gradient(cmap="Greens").format("{:.4f}"))
        st.caption("Valores em $pF/m$ (pico-Farad por metro).")
        
        # Susceptância Capacitiva (B = 2*pi*f*C) microsiemens/km
        # C (F/m) * 1000 = F/km
        B_mat = 2 * np.pi * freq * (C_mat * 1000) * 1e6 # em micro Siemens
        st.markdown("**Matriz de Susceptância Capacitiva ($\mu S/km$)**")
        st.dataframe(pd.DataFrame(B_mat, index=nomes, columns=nomes).style.format("{:.4f}"))
