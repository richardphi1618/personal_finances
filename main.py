from collections import defaultdict
from os import listdir, path, remove, scandir
from typing import List

import pandas as pd

# df = pd.read_csv (r'./data/shared_savings.CSV')
# print (df)

# assign directory
data_dir = "data"


def subdirs(directory: str) -> List[str]:
    output_list = []
    """Yield directory names not starting with '.' under given path."""
    for entry in scandir(f"./{directory}/"):
        if not entry.name.startswith(".") and entry.is_dir():
            output_list.append(entry.name)
    
    return output_list

def process_data(input_data_path: str, meta_data: dict):
    df_master= pd.DataFrame()
    for owner in meta_data:
        for account_type in meta_data[owner]:
            print(f"\n#### processing....owner:{owner}.....account_type:{account_type} ####\n")
            df = read_all_csv_to_df(f'./{input_data_path}/{owner}/{account_type}/')
            df['account_owner']=owner
            df['account_type']=account_type
            if df_master.empty: 
                df_master = df
            else:
                df_master = pd.concat([df_master, df], ignore_index = True)
    
    return df_master

def read_all_csv_to_df (dir: str):
    df_master= pd.DataFrame()
    for filename in listdir(dir):
        f = path.join(dir, filename)
        if path.isfile(f) and filename.endswith('.CSV'):
            print(f)
            df_new = pd.read_csv(f)
            #print(df_new)
            if df_master.empty: 
                df_master = df_new
            else:
                df_master = pd.concat([df_master, df_new], ignore_index = True)
    
    return df_master

def transaction_classifier ( df ):
    return df

if __name__=='__main__':

    master_raw_file_path = f'./{data_dir}/master_raw.csv'
    master_processed_file_path = f'./{data_dir}/master_processed.csv'


    if path.exists(master_raw_file_path): remove(master_raw_file_path)
    if path.exists(master_processed_file_path): remove(master_processed_file_path)

    meta_data = {}
    account_owners=subdirs(data_dir)

    for owner in account_owners:
        account_types=subdirs(f'{data_dir}/{owner}/')
        meta_data.update({owner:account_types})

    output = process_data(f"{data_dir}", meta_data)
    output = output.drop_duplicates()
    output.to_csv(master_raw_file_path)

    output.loc[output['Date'].isnull(),'Date'] = output['Transaction Date']
    output=output.drop(['No.','Transaction Date', 'Posted Date'], axis=1)
    output['Date'] = pd.to_datetime(output['Date'])

    output = transaction_classifier(output)

    print(output.info())
    output.to_csv(master_processed_file_path)
