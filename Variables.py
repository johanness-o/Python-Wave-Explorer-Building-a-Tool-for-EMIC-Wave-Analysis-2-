# import os.path
# from os.path import dirname, join as pjoin
# import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.io import readsav
import numpy as np
from matplotlib.colors import LogNorm
#  PORTING

# data_dir = pjoin(dirname(sio.__file__), 'tests', 'data')
# sav_fname = pjoin (data_dir, 'array_float32_1d.sav')
# sav_fname = '/Users/ojukwju1/IDL_Files/idl_test_file.sav'
# sav_fname = '/Users/ojukwju1/IDL_Files/mms_wavek_testfile.sav'
sav_fname = '/Users/ojukwju1/IDL_Files/mms2_bwaves_jwaves_20160116_1710_2010.sav'
sav_data = readsav(sav_fname)
print(sav_fname)
print('Variables in this . sav file: ')
print(sav_data.keys())
# print(sav_data['letters'])
# print(sav_data['decimals'])

# wtime = sav_data['wtime']
# kvec = sav_data['k_weighted'] * 1000
# kx = kvec[0, 0: kvec.shape[1]] # This call will put data into 1d arrays
# ky = kvec[1, 0: kvec.shape[1]]
# kz = kvec[2, 0: kvec.shape[1]]
# kangle = sav_data['kangle_weighted']
# fpk = sav_data['fpk_weighted']
bwave_time = sav_data['bwave_time']
# depedent varables (x,y,z)
bwave_x = sav_data['bwave_x']
bwave_y = sav_data['bwave_y']
bwave_z = sav_data['bwave_z']
# independent variable
bpower_time = sav_data['bpower_time']
bpower_freq = sav_data['bpower_freq']
# independent variable
bpower = sav_data['bpower']
jwave_time = sav_data['jwave_time']
jwave_x = sav_data['jwave_x']
jwave_y = sav_data['jwave_y']
jwave_z = sav_data['jwave_z']
jpower_time = sav_data['jpower_time']
jpower_freq = sav_data['jpower_freq']
jpower = sav_data['jpower']

fig, axs = plt.subplots(4)
fig.suptitle('Vertically Stacked Subplots')
ax = axs[0]
c = ax.plot(bwave_time, bwave_z)
ax = axs[1]
c = ax.pcolor(bpower, norm = LogNorm())
fig.colorbar(c, ax = ax)
ax = axs[2]
c = ax.plot(jwave_time, jwave_z)
ax = axs[3]
c = ax.pcolor(jpower, norm = LogNorm())
fig.colorbar(c, ax = ax)
plt.colorbar()
plt.show()

# c = ax0.pcolor(X, Y, Z, shading='auto',
#                norm=LogNorm(vmin=Z.min(), vmax=Z.max()), cmap='PuBu_r')
# fig.colorbar(c, ax=ax0)
#
# c = ax1.pcolor(X, Y, Z, cmap='PuBu_r', shading='auto')
# fig.colorbar(c, ax=ax1)
#
# plt.show()


# plt.scatter(kx,ky)
# plt.show()