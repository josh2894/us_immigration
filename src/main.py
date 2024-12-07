import os
from cleaning import imm_load_data, imm_rename_raw_cols, imm_obj_to_int, pres_rows_cols_filter, pres_rename_names
from utils import load_env_vars
import pandas as pd

def main():
    load_env_vars()
    
    df = imm_load_data() # Load the immigration dataset
    df = imm_rename_raw_cols(df) # Rename column names to more conventional
    df = imm_obj_to_int(df) # Correct data types
    
    presidents_csv = os.getenv('presidents_csv')
    df_presidents = pd.read_csv(presidents_csv) # Load the presidents dataset
    df_presidents = pres_rows_cols_filter(df_presidents) # Filter out unnecessary rows and columns
    df_presidents = pres_rename_names(df_presidents) # Change full names to common names
    
    df_joined = df.merge(df_presidents, on='year') # Combine the immigration and presidents datasets
    
    processed_data_dir = os.getenv('processed_data_dir')
    destination_path = os.path.join(processed_data_dir, 'us_immigration_final.csv')
    df_joined.to_csv(destination_path, index=False)
    
if __name__ == '__main__':
    main()

