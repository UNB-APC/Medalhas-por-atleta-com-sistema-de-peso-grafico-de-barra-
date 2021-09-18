import plotly.express as px
import pandas as pd
dados_df = pd.read_excel("dados.xlsx") #leitura dos dados

##Posição	Atleta	Pais	Modalidade	Anos	Jogos	Sexo	Ouro	Prata	Bronze	Total

atletas = []

for i in range(len(dados_df.values)):  
    atleta = {
        'nome': dados_df['Atleta'][i].replace('\xa0', ''),
        'ouro': dados_df['Ouro'][i],
        'prata': dados_df['Prata'][i],
        'bronze': dados_df['Bronze'][i]
       }
    atletas.append(atleta)
   
atletas= sorted(atletas, key=lambda item: (item["ouro"], item["prata"], item["bronze"]), reverse=True)

print(atletas)

fig = px.bar(
        atletas,
        title="Olimpíadas - Medalhas por atleta",  
        x= 'nome',
        y=['ouro','prata','bronze'], 
        color_discrete_map={'ouro':'gold','prata':'silver', 'bronze':'#eb7e24'}, 
        labels={'value':'Quantidades de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
        )
fig.show()
