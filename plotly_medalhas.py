
import plotly.express as px
import pandas as pd
dados_df = pd.read_excel("dados.xlsx") #leitura dos dados

##Posição	Atleta	Pais	Modalidade	Anos	Jogos	Sexo	Ouro	Prata	Bronze	Total

medalhas = {}
atletas = {'nome': [], 'ouro':[],'prata':[],'bronze':[]}

for i in range(len(dados_df.values)):   
    atletas['nome'].append(dados_df['Atleta'][i].replace('\xa0', ''))
    atletas['ouro'].append(dados_df['Ouro'][i])
    atletas['prata'].append(dados_df['Prata'][i])
    atletas['bronze'].append(dados_df['Bronze'][i])


fig = px.bar(
        atletas,
        title="Olimpíadas - Medalhas por atleta",  
        x= 'nome',
        y=['ouro','prata','bronze'], 
        color_discrete_map={'ouro':'gold','prata':'silver', 'bronze':'#eb7e24'}, 
        labels={'value':'Quantidades de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
        )
fig.show()