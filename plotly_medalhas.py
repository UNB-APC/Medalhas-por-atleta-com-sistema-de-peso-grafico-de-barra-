from pandas.core.frame import DataFrame
import plotly.express as px
import pandas as pd

#leitura dos dados
dados_csv = pd.read_csv("athlete_events.csv") 

#ID[0],"Name"[1],"Sex"[2],"Age"[3],"Height"[4],"Weight"[5],"Team"[6],"NOC"[7],"Games"[8],"Year"[9],"Season"[10],"City"[11],"Sport"[12],"Event"[13],"Medal"[14]

dados = {}

for linha in dados_csv.values:  
    if type(linha[14]) != str:
        continue
    nome= linha[1]
    ano= linha[9]
    medalha= linha[14]
    
    if dados.get(ano) == None:
        dados[ano] = {}
    if dados[ano].get(nome) == None:
        dados[ano][nome] = {'Gold': 0, 'Silver': 0, 'Bronze':0 }

    dados[ano][nome][medalha]+=1

anos_ordenados  = sorted(dados)

dataFrame= {'ano': [], 'atleta': [], 'medalhas':[]}
for ano in dados:
    for atleta in dados[ano]:
        dataFrame['ano'].append(ano)
        dataFrame['atleta'].append(atleta)
        dataFrame['medalhas'].append(dados[ano][atleta])

fig = px.bar(
        dataFrame,
        title="Olimpíadas - Medalhas por atleta",  
        x= dados['atletas'],
        y= [dados['Gold'],dados['Silver'],dados['Bronze']], 
        width=2009,
        
        labels={'value':'Quantidades de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
        )
fig.show()
