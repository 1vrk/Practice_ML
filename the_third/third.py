import pandas as pd
import chardet
import warnings

warnings.filterwarnings('ignore')

df = pd.read_excel('fs_test_data.xlsx')
print(df)