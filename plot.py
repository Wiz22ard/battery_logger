import pandas as pd 
import matplotlib.pyplot as plt 
import subprocess as sp
from datetime import datetime
import os
import glob

categories = ['voltage', 'temperature', 'percentage']
cat_path = "/data/data/com.termux/files/home/storage/termux/api/battery"

n_plots = len(categories)

fig, axs = plt.subplots(n_plots, 1, 
                        figsize = (20,5 * n_plots), 
                        dpi = 300, sharex = True)

fig.suptitle("Daily Battery Logger Plots",
             fontsize = 30,
             fontweight = 'bold',
             fontstyle = 'italic',
             y = .99)

for i, category in enumerate(categories):
    csv_files = glob.glob(os.path.join(cat_path, category, '*.csv'))
    
    df = pd.DataFrame()
    for csv_file in csv_files[1:]:
        df_temp = pd.read_csv(csv_file)
        df = pd.concat([df, df_temp], ignore_index = True)

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values(by='timestamp', inplace=True)
    """
    for val in df['status'].unique():
        subset = df.loc[df['status']==val]
        axs[i].scatter(subset['timestamp'], subset['value'], 
                       label=val, s = 5)
    """
    axs[i].plot(df['timestamp'], df['value'], lw=.5, c='C1')

    axs[i].set_ylabel(category.capitalize(), fontweight = 'bold')
    axs[i].set_xlim(df['timestamp'].min(), df['timestamp'].max())
    axs[i].set_ylim(df['value'].min(), df['value'].max())
    axs[i].grid(True)

plt.legend(loc = 'upper left', 
           bbox_to_anchor = (0,-.2,1,.102), 
           borderaxespad=0,
           ncols = len(df['status'].unique()), 
           mode = 'expand',
           frameon = False)
plt.tight_layout()

download_path = "/data/data/com.termux/files/home/storage/downloads"
plt.savefig(download_path + "/daily.png")
print("Daily Plot has been saved! in", download_path)
