import glob
from scipy import interpolate
import os
import numpy as np

folderpath = os.getcwd() + '/csv_number/'
resamplepath = os.getcwd() + '/csv_resampled/'

if not os.path.exists(resamplepath):
    os.mkdir(resamplepath)

Search_data_from = '.csv'
resampling_size = 10

filenamelist = []


filelist = glob.glob(folderpath + '/*' + Search_data_from)
# print(filelist)




for d in range(0, len(filelist), 1):
    data_original = np.loadtxt(filelist[d])
    f = interpolate.interp1d(data_original[:, 0], data_original[:, 1], fill_value="extraplate")
    data_transformed = np.linspace(0, data_original[-1, 0], resampling_size)

    resampling_data = np.column_stack((data_transformed, f(data_transformed)))
#
#         filenamelist = filenamelist + [os.path.splitext(os.path.basename(filelist[d]))[0]]
#
#         np.savetxt(resamplepath + filenamelist[d] + '_resampled' + '.csv', resampling_data)
#
# print(filelist)
# print(filenamelist)



