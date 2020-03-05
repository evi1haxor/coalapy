"""
all commands to dedicated files goes through this file of helper fnctions.
for example, 
"""

from . import similarity_mat as sm


def get_similarity(df_csv): #dfraem_csv obj
    if df_csv.path:
        print("don't give path yet ", df_csv.path)
        return matrix(df_csv = df_csv) #dframe_csv obj
    else:
        print("no paths. good ", df_csv.path)
    
        
def matrix(df_csv=None, W = None): #dfraem_csv obj
    if df_csv:
        if df_csv.mat_type == 'gaussian':
            return sm.Gaussian(df_csv.df, df_csv.df.shape[1])
    elif W is not None:
        return sm.get_degree(W)

def dist(i, j, df): #pandas df
    result_vector = df[list(df.columns)[i]] - df[list(df.columns)[j]]
    result_vector= result_vector * result_vector
    result = result_vector.sum()
    return result
