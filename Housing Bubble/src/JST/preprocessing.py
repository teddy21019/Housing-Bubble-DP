import pandas as pd
import numpy as np

def createRealPrice(dat: pd.DataFrame, nomvar: str):       # nomvar is the nominal variable in the dataset
    dat = dat[
        dat[nomvar].notnull() 
    ].copy()
    real_price_colname = "real_" + nomvar
    dat[real_price_colname] = np.log(dat[nomvar]/dat['cpi']) 

    return dat