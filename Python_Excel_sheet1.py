# separando só as sheet selecionada da planilha

import pandas as pd 

df = pd.read_excel("C:\DarioExercícios\Exercicio MOP - Exportação Dados Externo3.xlsx")

# Lista de elementos desejados
elementos_desejados = ['BMG', 'DECOLAR', 'LATAM', 'GLOVO', 'SANTANDER', 'SEM PARAR', 'SKY', 'TELEFONICA']

# Dicionário para armazenar os dataframes dos elementos
dfs = {}

# Iteração sobre os elementos desejados
for elemento in elementos_desejados:
    elemento_df = df.loc[df['cliente'] == elemento].copy()
    elemento_df.drop('cliente', axis=1, inplace=True)
    dfs[elemento] = elemento_df
    
# Gravação dos dataframes em abas separadas do arquivo Excel
with pd.ExcelWriter("C:\DarioExercícios\Exercicio MOP - Exportação Dados Externo2.xlsx") as writer:
    for elemento, df_elemento in dfs.items():
        df_elemento.to_excel(writer, sheet_name=elemento, index=False)
        
writer.save()