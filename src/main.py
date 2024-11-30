import os
from utils import load_env_vars
from cleaning import load_data, rename_raw_cols

df = load_data()
df = rename_raw_cols(df)
print(df)