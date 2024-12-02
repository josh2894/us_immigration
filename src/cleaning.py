import pandas as pd
import os
from utils import load_env_vars

def load_data():
    """
    Load data from csv into dataframe
    
    Returns:
        df (pd.DataFrame): loaded dataset
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
        df_renamed (pd.DataFrame): renamed dataframe
    """
    df_renamed = df_raw.rename(columns={'Immigrants Obtaining Lawful Permanent Resident Status': 'lawful_permanent_resident_obt',
                   'Refugee Arrivals': 'refugee_arrivals',
                   'Noncitizen Apprehensions': 'noncitizen_apprehensions',
                   'Noncitizen Removals': 'noncitizen_removals',
                   'Noncitizen Returns': 'noncitizen_returns'})
    return df_renamed


def obj_to_int(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts the object columns into integer columns
    
    Args:
        df (pd.DataFrame): dataframe before data types are converted

    Returns:
        df (pd.DataFrame): dataframe with converted data types
    """
    df.replace(',', '', regex=True, inplace=True)
    obj_cols = df.select_dtypes(include='object').columns.to_list()
    df[obj_cols] = df[obj_cols].astype('int')
    return df