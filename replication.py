
import pandas as pd

# Replace 'your_file.dta' with the path to your Stata file
df = pd.read_stata('users/ritvik/desktop/Reply-to-Albouy-dataset-for-AER-replication-filing-May-2-2012.dta')
df = pd.read_stata('users/ritvik/desktop/table3a.do')
df = pd.read_stata('users/ritvik/desktop/table3b.do')
df = pd.read_stata('users/ritvik/desktop/table2a.do')
df = pd.read_stata('users/ritvik/desktop/table2b.do')
df = pd.read_stata('users/ritvik/desktop/table1a.do')
df = pd.read_stata('users/ritvik/desktop/table1b.do')
df = pd.read_stata('users/ritvik/desktop/figure1.do')




# Replace 'your_new_file.csv' with the desired path for your new CSV file
df.to_csv('users/ritvik/desktop/Fig1a.csv', index=False)
df.to_csv('users/ritvik/desktop/Fig1b.csv', index=False)

# Selecting key variables of interest
key_variables = ['longname', 'mort', 'logmort0', 'loggdp', 'latitude', 'africa', 'neoeuro']
df_key = df[key_variables]

print(df_key.head())