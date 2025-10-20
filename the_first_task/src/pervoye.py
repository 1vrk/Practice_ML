import pandas as pd
import chardet
import warnings


warnings.filterwarnings('ignore')

def analyze_file(filename):

    with open(filename, 'rb') as f:
        encoding = chardet.detect(f.read())['encoding']

    for sep in ['\t']:
        try:
            df_sample = pd.read_csv(filename, sep=sep, encoding=encoding)
            print(df_sample.head())
            df_sample.to_csv('../data/data_prep.csv', index=False)
        except:
            continue


analyze_file('../data/data_prep.tab')

df = pd.read_csv('../data/data_prep.csv')
print(df)

df['AVG_LATENCY'].fillna(df['AVG_LATENCY'].median(), inplace = True)
df['MIN_LATENCY'].fillna(df['MIN_LATENCY'].median(), inplace = True)
df['MAX_LATENCY'].fillna(df['MAX_LATENCY'].median(), inplace = True)


df['GROUP_CHANGE_RESULT'].fillna(df['GROUP_CHANGE_RESULT'].median(), inplace = True)
df['PROFIT_GROUP_ID'].fillna(df['PROFIT_GROUP_ID'].median(), inplace = True)
df['CHANGE_PROFIT_GROUP_ID'].fillna(df['CHANGE_PROFIT_GROUP_ID'].median(), inplace = True)
df['CHANGE_SEGMENT_ID'].fillna(df['CHANGE_SEGMENT_ID'].median(), inplace = True)
df['PVAL_GROUP_CHANGE0'].fillna(df['PVAL_GROUP_CHANGE0'].median(), inplace = True)
df['PVAL_GROUP_CHANGE1'].fillna(df['PVAL_GROUP_CHANGE1'].median(), inplace = True)
df['PVAL_GROUP_CHANGE_1'].fillna(df['PVAL_GROUP_CHANGE_1'].median(), inplace = True)

df.to_csv('data_prep_rdy.csv', index=False)

print(df)
def create_lag_features_pandas(input_file='data_prep_rdy.csv', output_file='result_data_preb.csv'):
    df = pd.read_csv(input_file)
    columns_to_lag = [col for col in df.columns if col not in ['CLIENT_ID', 'SEGM_DATE']]

    result_df = [df[['CLIENT_ID', 'SEGM_DATE']].copy()]

    for col in columns_to_lag:
        temp_df = pd.DataFrame()

        temp_df[col] = df[col]

        temp_df[f'{col}_1'] = df.groupby('CLIENT_ID')[col].shift(1)

        temp_df[f'{col}_2'] = df.groupby('CLIENT_ID')[col].shift(2)

        result_df.append(temp_df)

    final_df = pd.concat(result_df, axis=1)

    final_df.to_csv(output_file, index=False)
    return final_df

results_df = create_lag_features_pandas()
print(results_df)
