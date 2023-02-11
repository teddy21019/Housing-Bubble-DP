import pandas as pd
from src.Filter import FilterLayer


class BubbleDetector:
    def __init__(self, df:pd.DataFrame, filter: FilterLayer) -> None:
        

        self.df = df
        self.filter = filter

        if not self.validate(self.df):
            raise ValueError("Bubble dataframe loader returns invalidated structure. Must have both columns named \"time\" and \"price\"")
        
        self.bubble_df = self.generate_bubble()


    @staticmethod
    def create_band(dat: pd.DataFrame):
        std = dat['cycle'].std() 
        dat['upper'] = dat['trend'] + std 
        dat['lower'] = dat['trend'] - std
        dat['is_bubble'] = dat["price"] > dat['upper']
        return dat

    @staticmethod
    def validate(df:pd.DataFrame):
        if not {'time', 'price'}.issubset(set(df.columns)):
            return False
        return True


    def generate_bubble(self):

        return(self.df
                .pipe(self.filter.filter_func)
                .pipe(self.create_band)
            )