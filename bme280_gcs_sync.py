import subprocess
import os

raspi_folder = os.getcwd()

# print(raspi_folder)

folder_name1 = 'graph_datas'
folder_name2 = 'csv_datas'


subprocess.run('rclone sync ' + raspi_folder + '/' + folder_name1 + ' gcs:' + 'practice_yasuilabo/hara/' + folder_name1, shell=True)
subprocess.run('rclone sync ' + raspi_folder + '/' + folder_name2 + ' gcs:' + 'practice_yasuilabo/hara/' + folder_name2, shell=True)

print('finished')