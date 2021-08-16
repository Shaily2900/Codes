import pandas as pd
file= pd.ExcelFile("\Users\91704\Downloads\sales.xlsx")
print(file.sheet_names)
['sales','customers']
sheet=file.parse('sales')
print(sheet)
