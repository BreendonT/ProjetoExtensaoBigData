import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Carregar dados do Excel
df = pd.read_excel('data/barbearia_frequencia_junho_final.xlsx')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Contagem de atendimentos por dia da semana
atendimentos_por_dia = df['Dia'].value_counts()
print(atendimentos_por_dia)

# Contagem de atendimentos por barbeiro
atendimentos_por_barbeiro = df['Barbeiro'].value_counts()
print(atendimentos_por_barbeiro)

# Configurações de estilo
sns.set(style="whitegrid")

# Gráfico de barras - Atendimentos por Dia da Semana
plt.figure(figsize=(10, 6))
sns.barplot(x=atendimentos_por_dia.index, y=atendimentos_por_dia.values, palette='viridis')
plt.title('Atendimentos por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Atendimentos')
plt.xticks(rotation=45)
plt.show()

# Gráfico de barras - Atendimentos por Barbeiro
plt.figure(figsize=(10, 6))
sns.barplot(x=atendimentos_por_barbeiro.index, y=atendimentos_por_barbeiro.values, palette='viridis')
plt.title('Atendimentos por Barbeiro')
plt.xlabel('Barbeiro')
plt.ylabel('Número de Atendimentos')
plt.show()

# Gráfico interativo - Atendimentos ao Longo do Tempo
fig = px.line(df, x='Data', y='Hora', color='Barbeiro', title='Atendimentos ao Longo do Tempo')
fig.show()
