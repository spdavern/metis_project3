import pandas as pd

def run():
    #"Obtain: downloading raw data files..."
    return None

def load_map_df_from_csv(start_year,end_year):
    data_folder = './data/raw/'
    filename_common = '_ADR-301-MAP-Assessment-Scores.csv'
    map_df = None
    for yr in range(start_year,end_year+1):
        df = pd.read_csv(data_folder+str(yr)+filename_common, encoding = "ISO-8859-1")
        if map_df is None:
            map_df = df.copy()
        else:
            map_df = map_df.append(df, ignore_index = True).copy()
    return map_df