# """modalities here"""
# import src

# W=[[-1, 3, 5], [9, 4, 2], [6, 2, -6]]

# # print (W)
# # m = modalities.modality(W)
# # path = None
# # df = src.dfhandler.dframe_csv(path, mat_type='gaussian')
# df = src.modalities.modality( mat_type="gaussian")
# print(df.W)\
import src.modalities as modality
import numpy as np

path = '/hdd/Ztudy/BTP/code/mi.csv'

try:
    x1= modality.modality(path, mat_type="gaussian")
    print("made x1")
except: 
    print("NO PATH PROVIDED")
# print(x1.degree, '\n', x1.W, '\n', x1.laplacian)
# np.savetxt("yo.csv", x1.laplacian, delimiter = ',')