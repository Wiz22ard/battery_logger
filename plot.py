import pandas as pd 
import matplotlib.pyplot as plt 
import subprocess as sp
from datetime import datetime
import os

files = ['voltage', 'temperature', 'percentage']

for file in files:
    date_str = datetime.now().strftime('%Y-%m-%d')
    csv_file = os.path.join(file, date_str) + '.csv'
    df = pd.read_csv(csv_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values(by='timestamp', inplace=True)

    fig = plt.figure(figsize=(20,5), dpi=300)
    for val in df['status'].unique():
        subset = df.loc[df['status']==val]
        plt.plot(subset['timestamp'], subset['value'], label=val)
    
    plt.title(f"{file.upper()} Daily Plot", 
              {'fontsize': 36, 'fontweight':'bold'}, 
              pad=12)
    plt.ylabel(file)
    plt.xlim(df['timestamp'].min(), df['timestamp'].max())
    plt.ylim(df['value'].min(), df['value'].max())
    plt.grid(True)
    plt.legend()
    plt.savefig(f"/data/data/com.termux/files/home/storage/downloads/{file}.png")
    print(csv_file)
