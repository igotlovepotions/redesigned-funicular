# Planejamento do Projeto

## Visão Geral
O objetivo deste projeto é calcular parâmetros elétricos de linhas de transmissão (indutância, capacitância, impedância, etc.) a partir da geometria da torre e das características dos cabos.

## Estado Atual
- **`calculo_RLC.py`**: Realiza cálculos básicos de parâmetros (Zs, Zc, SIL) baseados em valores fixos/estimados de L e C.
- **`mostrar_cabos.py`**: Visualiza a posição dos cabos em um gráfico e calcula distâncias euclidianas entre eles.
- **`calculo_de_parametros.py`**: Tenta implementar o cálculo matricial de indutâncias, mas está incompleto e com erros de sintaxe (depende de variáveis não definidas).

## Plano de Ação

### 1. Reestruturação e Padronização
- [ ] **Organizar arquivos**: Criar uma estrutura de projeto mais limpa (ex: pasta `src/` ou módulos definidos).
- [ ] **Configuração Centralizada**: Criar um arquivo (ex: `config.py` ou `geometria.py`) para definir a posição dos cabos e características físicas. Isso evitará duplicação de dados entre o script de visualização e o de cálculo.
- [ ] **Gestão de Dependências**: Criar um `requirements.txt` (numpy, matplotlib).

### 2. Implementação do Motor de Cálculo (`engine`)
- [ ] **Corrigir `calculo_de_parametros.py`**:
    - Importar a geometria corretamente.
    - Implementar algorítmo para calcular todas as distâncias mútuas ($D_{ij}$) automaticamente.
    - Corrigir a montagem da matriz de indutância ($L$) usando o método das imagens (Carson/Condutores de imagem).
    - Implementar o cálculo da matriz de capacitância ($C$) (potencial de Maxwell).
- [ ] **Cálculo de Parâmetros de Sequência**: Obter as impedâncias de sequência zero e positiva a partir das matrizes de fase.

### 3. Interface e Integração
- [ ] **Script Principal**: Criar um `main.py` que unifique o fluxo:
    1. Carregar dados.
    2. Exibir geometria (opcional).
    3. Executar cálculos.
    4. Exibir resultados formatados de forma clara.

### 4. Validação
- [ ] Verificar os resultados com exemplos conhecidos de literatura ou dados teóricos.
