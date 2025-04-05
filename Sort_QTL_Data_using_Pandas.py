# My cousin had a file that had data of Traits marked on a chromosome derived from various sources
# This is simple Pandas sorting excercise to sort and seggregate data belonging to same source and sorted basis position on chromosomes

import pandas as pd

# Read the entire Excel file
df = pd.read_excel("marker.xlsx")

# Display the first few rows of the dataframe

df = df[['Marker','Chr.','Position','Source']]
df["Source"] = df["Source"].fillna(method="ffill")
df=df[df['Chr.'].notna()]
df.loc[df["Source"] == 7, "Source"] = "Qin et al., 2010"
df['Source'] = df['Source'].str.replace(' ','')
df['Source'] = df['Source'].str.replace(',','')
df['Source'] = df['Source'].str.replace('.','')
df['Source'] = df['Source'].str.replace('(','')
df['Source'] = df['Source'].str.replace(')','')
df['Source'] = df['Source'].str.replace('{','')
df['Source'] = df['Source'].str.replace('}','')




df2 = pd.read_excel("qtl data 2.xlsx")
df2["SOURCE"] = df2["SOURCE"].fillna(method="ffill")
# df2=df2[df2['CHROMOSOME NO.']==True]
df2 = df2[['QTL','CHROMOSOME NO.','POSITION OF QTL','SOURCE']]
df2=df2[df2['CHROMOSOME NO.'].notna()]
df2.rename(columns={'QTL': 'Marker', 'CHROMOSOME NO.': 'Chr.','POSITION OF QTL':'Position','SOURCE':'Source'}, inplace=True)
df2['Source'] = df2['Source'].str.replace(' ','')
df2['Source'] = df2['Source'].str.replace(',','')
df2['Source'] = df2['Source'].str.replace('.','')
df2['Source'] = df2['Source'].str.replace('(','')
df2['Source'] = df2['Source'].str.replace(')','')
df2['Source'] = df2['Source'].str.replace('{','')
df2['Source'] = df2['Source'].str.replace('}','')




df_merged = pd.concat([df,df2])
df_final = df_merged.sort_values(["Chr.", "Position", "Source"])
df_final.to_csv('fold/data_final.csv')
print(df_final.head(50))import pandas as pd

# Read the entire Excel file
df = pd.read_excel("marker.xlsx")

# Display the first few rows of the dataframe

df = df[['Marker','Chr.','Position','Source']]
df["Source"] = df["Source"].fillna(method="ffill")
df=df[df['Chr.'].notna()]
df.loc[df["Source"] == 7, "Source"] = "Qin et al., 2010"
df['Source'] = df['Source'].str.replace(' ','')
df['Source'] = df['Source'].str.replace(',','')
df['Source'] = df['Source'].str.replace('.','')
df['Source'] = df['Source'].str.replace('(','')
df['Source'] = df['Source'].str.replace(')','')
df['Source'] = df['Source'].str.replace('{','')
df['Source'] = df['Source'].str.replace('}','')




df2 = pd.read_excel("qtl data 2.xlsx")
df2["SOURCE"] = df2["SOURCE"].fillna(method="ffill")
# df2=df2[df2['CHROMOSOME NO.']==True]
df2 = df2[['QTL','CHROMOSOME NO.','POSITION OF QTL','SOURCE']]
df2=df2[df2['CHROMOSOME NO.'].notna()]
df2.rename(columns={'QTL': 'Marker', 'CHROMOSOME NO.': 'Chr.','POSITION OF QTL':'Position','SOURCE':'Source'}, inplace=True)
df2['Source'] = df2['Source'].str.replace(' ','')
df2['Source'] = df2['Source'].str.replace(',','')
df2['Source'] = df2['Source'].str.replace('.','')
df2['Source'] = df2['Source'].str.replace('(','')
df2['Source'] = df2['Source'].str.replace(')','')
df2['Source'] = df2['Source'].str.replace('{','')
df2['Source'] = df2['Source'].str.replace('}','')




df_merged = pd.concat([df,df2])
df_final = df_merged.sort_values(["Chr.", "Position", "Source"])
df_final.to_csv('fold/data_final.csv')
print(df_final.head(50))