import pandas as pd
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')
feature_columns = df.columns[:9]
target_column = df.columns[10]
X = df[feature_columns]
y = df[target_column]
correlations = X.corrwith(y)
sorted_correlations = correlations.abs().sort_values(ascending=False)
print(sorted_correlations)
