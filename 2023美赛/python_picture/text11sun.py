import plotly.express as px
import pandas as pd

# Read two Excel files
df1 = pd.read_excel('origin11_end.xlsx')
df2 = pd.read_excel('origin22_end.xlsx')

# Add IDs for two data frames_ Col column
df1['id_col'] = 'Monohulled Sailboats'
df2['id_col'] = 'Catamarans'

# Merge two data frames
df = pd.concat([df1, df2])

# Create a Sunrise Chart
fig = px.sunburst(
    df,
    path=['id_col', 'Make'],
    values='count',
    color='Make',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# Display Sunrise Chart
fig.show()
