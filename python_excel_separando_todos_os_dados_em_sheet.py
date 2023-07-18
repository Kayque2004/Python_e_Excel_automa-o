# separando todos os dados em sheet. 
import pandas as pd

# Carregar a planilha em um DataFrame
df = pd.read_excel('Exercicio MOP - Exportação Dados Externo.xlsx')

# Obter valores únicos da coluna que será usada para separar em abas
coluna_separadora = 'cliente'
valores_unicos = df[coluna_separadora].unique()

# Criar um novo arquivo Excel
writer = pd.ExcelWriter('SegundoPlano_Exportação Dados Externo1.xlsx')

# Separar os dados em abas separadas
for valor in valores_unicos:
    # Filtrar os dados com base no valor da coluna separadora
    df_filtrado = df[df[coluna_separadora] == valor]
    
    # Escrever os dados na aba correspondente
    df_filtrado.to_excel(writer, sheet_name=str(valor), index=False)

# Fechar o escritor de Excel
writer.save()