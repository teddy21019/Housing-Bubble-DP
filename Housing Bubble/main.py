from functools import partial
import pandas as pd
import numpy as np
from src.DFPreprocessor import JSTDataFrameLoader
from src.BubbleDetector import BubbleDetector
from src.Filter import HPFilter
from typing import List

jst_file_path = "data\JSTdatasetR5.xlsx"

def createRealPrice(dat: pd.DataFrame, nomvar: str):       # nomvar is the nominal variable in the dataset
    dat = dat[
        dat[nomvar].notnull() 
    ].copy()
    real_price_colname = "real_" + nomvar
    dat[real_price_colname] = np.log(dat[nomvar]/dat['cpi']) 

    return dat


def main():

    country_code = 'USA'
    df_loader = JSTDataFrameLoader(data_path=jst_file_path,
                                    country=country_code)   \
                .pre_transform(partial(createRealPrice, nomvar='gdp'))       \
                .set_time_price(
                    time_column='year', 
                    price_column='real_gdp'
                    )

    trend_filter = HPFilter(llambda = 100, freq='Y')

    bubble = BubbleDetector(df_loader.get_dataframe(), trend_filter)

    print(bubble.bubble_df)
   ## Do something about bubble 







if __name__ == "__main__":
    main()