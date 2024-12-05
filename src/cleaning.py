import pandas as pd
import os
from utils import load_env_vars


def imm_load_data():
    """
    Load data from csv into dataframe
    
    Returns:
        df (pd.DataFrame): loaded dataset
    """
    load_env_vars()
    us_immigration_csv = os.getenv("us_immigration_csv")
    df = pd.read_csv(us_immigration_csv)
    return df
    
    
def imm_rename_raw_cols(df_raw: pd.DataFrame) -> pd.DataFrame:
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
                   'Noncitizen Returns': 'noncitizen_returns',
                   'Year': 'year'})
    return df_renamed


def imm_obj_to_int(df: pd.DataFrame) -> pd.DataFrame:
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


def pres_rows_cols_filter(df_presidents: pd.DataFrame) -> pd.DataFrame:
    """
    Filter out rows and columns based on what's necessary

    Args:
        df_presidents (pd.DataFrame): dataframe before filters are applied

    Returns:
        df_presidents (pd.DataFrame): dataframe after filters are applied
    """
    df_presidents = df_presidents[df_presidents['position_title'] == 'PRESIDENT OF THE UNITED STATES']
    df_presidents = df_presidents[df_presidents['year'] >= 1980]
    df_presidents = df_presidents.loc[:, :'term']
    return df_presidents


def pres_rename_names(df_presidents: pd.DataFrame) -> pd.DataFrame:
    """
    Rename president names to their common names

    Args:
        df_presidents (pd.DataFrame): dataframe with full president names

    Returns:
        df_presidents (pd.DataFrame): dataframe with president common names
    """
    df_presidents['name'] = df_presidents['name'].replace('Carter,Jimmy Earl,Jr.', 'Jimmy Carter')
    df_presidents['name'] = df_presidents['name'].replace('Reagan,Ronald Wilson', 'Ronald Reagan')
    df_presidents['name'] = df_presidents['name'].replace('Bush,George Herbert Walker', 'George H.W. Bush')
    df_presidents['name'] = df_presidents['name'].replace('Clinton,William Jefferson', 'Bill Clinton')
    df_presidents['name'] = df_presidents['name'].replace('Bush,George Walker', 'George W. Bush')
    df_presidents['name'] = df_presidents['name'].replace('Obama,Barack Hussein,II', 'Barack Obama')
    df_presidents['name'] = df_presidents['name'].replace('Trump,Donald John', 'Donald Trump')
    
    df_presidents.rename(columns={'name': 'president'}, inplace=True)
    return df_presidents
