import os
from cleaning import load_data, rename_raw_cols, obj_to_int
from utils import load_env_vars

def main():
    load_env_vars()
    
    df = load_data()
    df = rename_raw_cols(df)
    df = obj_to_int(df)
    
    processed_data_dir = os.getenv('processed_data_dir')
    destination_path = os.path.join(processed_data_dir, 'cleaned_us_immigration_data.csv')
    df.to_csv(destination_path, index=False)
    
if __name__ == '__main__':
    main()

