import pandas as pd
import numpy as np
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')
columns_to_transform = df.columns[:9]
X = df[columns_to_transform]
X_transformed = np.log1p(X)
X_transformed_df = pd.DataFrame(X_transformed, columns=columns_to_transform)
other_columns = df.columns[9:]
transformed_df = pd.concat([X_transformed_df, df[other_columns].reset_index(drop=True)], axis=1)
output_excel_file = 'outputone.xlsx'
transformed_df.to_excel(output_excel_file, index=False)
