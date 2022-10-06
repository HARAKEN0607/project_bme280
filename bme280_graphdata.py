import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# read csv data
csv_path = os.getcwd() + '/csv_data/' + 'data_20221005132502.csv'
csv_df = pd.read_csv(csv_path)

data_y1 = csv_df[csv_df.columns[1]]
data_y2 = csv_df[csv_df.columns[2]]
data_y3 = csv_df[csv_df.columns[3]]
data_x = np.linspace(0, len(data_y1), len(data_y1))

# Create figure base
fig = plt.figure(figsize=(10, 7), dpi=300)
ax1 = fig.add_subplot(3, 1, 1)               # Temperature figure
ax2 = fig.add_subplot(3, 1, 2)               # Pressure figure
ax3 = fig.add_subplot(3, 1, 3)               # Humidity figure

# plot data
ax1.plot(data_x/60, data_y1, linestyle='solid')
ax2.plot(data_x/60, data_y2, linestyle='solid')
ax3.plot(data_x/60, data_y3, linestyle='solid')

# set labels
ax3.set_xlabel('Time[min]', fontsize=15)
ax1.set_ylabel('Temperature[℃]', fontsize=15)
ax2.set_ylabel('Pressure[hPa]', fontsize=15)
ax3.set_ylabel('Humidity[%]', fontsize=15)

# set griding
ax1.grid(color='k', linestyle='dotted', linewidth=1)
ax2.grid(color='k', linestyle='dotted', linewidth=1)
ax3.grid(color='k', linestyle='dotted', linewidth=1)

# set scales range
ax1.set_xlim([0, 60])
ax2.set_xlim([0, 60])
ax3.set_xlim([0, 60])

ax1.set_ylim([22.7, 23.7])
ax2.set_ylim([1011.6, 1012.3])
ax3.set_ylim([41.8, 46.7])

# Disable Offset display(y_Pressure)
ax2.get_yaxis().get_major_formatter().set_useOffset(False)

# Graphs Drawing
plt.show()

# Graphs Saving
graph_path = os.getcwd() + '/graph_datas/'

if not os.path.exists(graph_path):
    os.mkdir(graph_path)

fig.savefig(graph_path + 'Weather_data_20221005132502.png')



