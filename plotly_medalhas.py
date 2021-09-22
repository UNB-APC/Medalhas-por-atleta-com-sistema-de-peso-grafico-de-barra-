import plotly.express as px
import pandas as pd

#leitura dos dados
dados_df = pd.read_csv("athlete_events.csv") 

#ID[0],"Name"[1],"Sex"[2],"Age"[3],"Height"[4],"Weight"[5],"Team"[6],"NOC"[7],"Games"[8],"Year"[9],"Season"[10],"City"[11],"Sport"[12],"Event"[13],"Medal"[14]

anos = {}

for linha in dados_df.values:  
    if type(linha[14]) != str:
        continue
    nome= linha[1]
    ano= linha[9]
    medalha= linha[14]
    
    if anos.get(ano) == None:
        anos[ano] = {}
    if anos[ano].get(nome) == None:
        anos[ano][nome] = {'Gold': 0, 'Silver': 0, 'Bronze':0 }

    anos[ano][nome][medalha]+=1

anoslist = list(anos.keys())
anoslist.sort()


 
dados = {
    'atletas' : [],
    'Gold' : [],  
    'Silver' : [],  
    'Bronze' : []  
}
for j in range(len(anos[1992])): 
        dados['atletas'].append(list(anos[1992].keys())[j])
        dados['Gold'].append(list(anos[1992].values())[j]['Gold'])
        dados['Silver'].append(list(anos[1992].values())[j]['Silver'])
        dados['Bronze'].append(list(anos[1992].values())[j]['Bronze'])


fig = px.bar(
        dados,
        title="Olimpíadas - Medalhas por atleta",  
        x= dados['atletas'],
        y= [dados['Gold'],dados['Silver'],dados['Bronze']], 
        width=2009,
        
        labels={'value':'Quantidades de medalhas', 'variable':'Medalhas', 'nome':'Atletas'}    
        )
fig.show()
