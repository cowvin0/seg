import pandas as pd

df = pd.read_csv('relacionamento_clusters.csv', dtype={'cod_carteira': str})

df1 = df.iloc[:50000, :]
df2 = df.iloc[50000:100000, :]
df3 = df.iloc[100000:150000, :]
df4 = df.iloc[150000:, :]
prods = df.columns[
            ~df.columns.str.startswith('prod_')
        ].tolist()

dfs = [
    i.set_index(prods).stack().to_frame().reset_index()
    for i in [df1, df2, df3, df4]
]

# Concatenando todos os DataFrames processados
result = pd.concat(dfs, ignore_index=True)

for i in [df1, df2, df3, df4]:
    dfs.append(
        i
        .set_index(prods)\
        .stack()\
        .to_frame()\
        .reset_index()
    )

df1 = df1\
    .set_index(prods)\
    .stack()#\
    #.to_frame()\
    #.reset_index()
