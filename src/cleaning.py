import pandas as pd
import os
from utils import load_env_vars

def load_data():
    """
    Load data from csv into dataframe
    
    Returns:
        pd.DataFrame: loaded dataset
    """
    load_env_vars()
    us_immigration_csv = os.getenv("us_immigration_csv")
    df = pd.read_csv(us_immigration_csv)
    return df
    
    
def rename_raw_cols(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Rename the columns from the raw data into conventional names
    Args:
        df_raw (pd.DataFrame): raw dataframe loaded from csv

    Returns:
        pd.DataFrame: renamed dataframe
    """
    df_raw.rename(columns={'Immigrants Obtaining Lawful Permanent Resident Status': 'lawful_permanent_resident_obt',
                   'Refugee Arrivals': 'refugee_arrivals',
                   'Noncitizen Apprehensions': 'noncitizen_apprehensions',
                   'Noncitizen Removals': 'noncitizen_removals',
                   'Noncitizen Returns': 'noncitizen_returns'}, inplace=True)
    return df_raw


    