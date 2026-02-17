import plotly.express as px
import plotly.data as pldata


df = pldata.wind(return_type='pandas')

df["strength"] = df["strength"].str.replace("\+", "", regex=True)
df["strength"] = df["strength"].str.replace("-.*", "", regex=True)
df["strength"] = df["strength"].astype(float)


fig = px.scatter(df, 
                 x='strength', 
                 y='frequency', 
                 color='direction',
                 title="Wind: Strength vs Frequency", 
                 hover_data=["direction", "strength", "frequency"])
fig.write_html("wind.html", auto_open=True)



#print(df.head(10))

#print(df.tail(10))
#print(df["strength"].head(10))
#print(df["strength"].dtype)