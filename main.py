import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('countyincome.csv')


values = df_sample['Per capita income'].tolist()
fips = df_sample['County'].tolist()


df_sample = pd.read_csv('countycode.csv')


state = df_sample['State FIPS Code'].tolist()
county = df_sample['County FIPS Code'].tolist()
name = df_sample['Short County Name'].tolist()

countyfip={}
for i in range(len(county)):
    county[i]=str(county[i])
    if len(county[i])==1:
        county[i]="00"+county[i]
    if len(county[i])==2:
        county[i]="0"+county[i]
    county[i]="42"+county[i]
    countyfip[name[i]]=county[i]

values1=[]
fips1=[]
for i in range(len(values)):
    if fips[i] in countyfip:
        values1.append(int(values[i][1:3]+values[i][4:]))
        fips1.append(countyfip[fips[i]])


print(values1)
print(fips1)



colorscale = [
"#f7fbff","#d2e3f3","#9ecae1","#57a0ce","#2171b5",
              "#08519c","#08306b"
]

fig = ff.create_choropleth(
    fips=fips1, values=values1, scope=['PA', 'OH', 'WV', 'NY', 'NJ','MD'],
    binning_endpoints=[14000,20600,22800,23000, 27049], colorscale=colorscale,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='per capita income by county($)', title='Per Capita Income by counties in Pennsylvania'
)
print(fips)
fig.layout.template = None
fig.show()
