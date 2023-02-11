
from src.df_preprocessor import BubbleDataFrameLoader
import pandas as pd
from src.filter import FilterLayer


class BubbleDetector:
    def __init__(self, bubble_df_loader: BubbleDataFrameLoader, filter: FilterLayer) -> None:
        
        self.bubble_df_loader = bubble_df_loader
        self.filter = filter

        # extract the processed data from df_loader
        self.df = self.bubble_df_loader.get_dataframe()

        if not self.validate():
            raise ValueError("Bubble dataframe loader returns invalidated structure. Must have both columns named \"time\" and \"price\"")
        
        self.bubble_df = self.generate_bubble()


    @staticmethod
    def create_band(dat: pd.DataFrame):
        std = dat['cycle'].std() 
        dat['upper'] = dat['trend'] + std 
        dat['lower'] = dat['trend'] - std
        dat['is_bubble'] = dat["price"] > dat['upper']
        return dat


    def validate(self):
        if not {'time', 'price'}.issubset(set(self.df.columns)):
            return False
        return True


    def generate_bubble(self):

        return(self.df
                .pipe(self.filter.filter_func)
                .pipe(self.create_band)
            )