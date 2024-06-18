import pandas as pd

# Carregar o arquivo CSV corrigido com vírgula como delimitador
caminho_arquivo_corrigido = 'focos_br_ref_2004.csv'
df = pd.read_csv(caminho_arquivo_corrigido, delimiter=',')

# Salvar o dataframe em um arquivo Excel
arquivo_excel_saida = 'focos_br_ref_2004_corrigido.xlsx'
df.to_excel(arquivo_excel_saida, index=False, engine='openpyxl')

print(f"O arquivo CSV foi corrigido e salvo como {arquivo_excel_saida}")
