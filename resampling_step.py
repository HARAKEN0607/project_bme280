import os
import csv
import numpy as np

csv_path = os.getcwd() + '/csv_data/'

file_name = 'data_20221005132502.csv'

# folder&file sitei
file_path = os.path.join(csv_path, file_name)

resample_name = 'data_20221005132502_resampled'

def data_reading(file_path):
    with open(file_path, 'r') as f:
        data = csv.reader(f)
        data_list = list(data)
        # reformat to 2D
        data_array = np.array(data_list)
        # selected_data = data_array[:, type]

        return data_array

data_array_original = data_reading(file_path)

result = []
result.append(['Time', 'Temperature', 'Pressure', 'Humid'])

resampling_size = 1000

resampling_interval = len(data_array_original)//resampling_size

# gyou goto ni kankaku wo akete toridasi
for d in range(0, len(data_array_original), resampling_interval):
    result.append(data_array_original[d, :])

# print(result)

with open(csv_path + resample_name + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)


# print(data_transformed)


