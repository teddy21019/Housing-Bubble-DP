from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from typing import Callable, List
from src.typing_alias import DataPipe

class BubbleDataFrameLoader(ABC):
    """
        Abstract class for pd.Dataframe loader
    """

    @abstractmethod
    def get_dataframe(self) -> pd.DataFrame:
        """
        Returns the dataframe associated with the given data_loader
        """
        ...
    
    @abstractmethod
    def pre_transform(self, pipe_function) -> pd.DataFrame:
        ...

    @abstractmethod
    def set_time_price(self, time_column:str, price_column:str):
       pass 


class JSTDataFrameLoader(BubbleDataFrameLoader):
    """
    Reads an JST macroeconomic database and filters the 
    information based on the country and extracts the time and price column
    """
    def __init__(self, 
                jst_df: pd.DataFrame ,
                country: str):

        """
            The constructor of a Dataframe loader specifically for 
            the JST database.


            Parameters
            ==========
            data_loader : DataLoader
                The DataLoader class that loads the JST database.
                This functionality is extracted in case the format of the 
                JST database is altered in the future for some reason. 
            
            country: str 
                The country to filter. Comes in the case of a country code.

            price_column: str
                The column of the price that is wanted. 
                Note that one might need to do some transformation, i.e. deflation or 
                getting the percentage change before assigning. 
        """
        self.df = jst_df 
        self.df = self.df[self.df['iso'] == country]




    def pre_transform(self, pipe_function:DataPipe) -> JSTDataFrameLoader:
        self.df = pipe_function(self.df)
        return self

    def set_time_price(self, time_column:str, price_column:str) -> JSTDataFrameLoader:
        rename_dict = {
            time_column:"time",
            price_column:"price"
        }

        self.df:pd.DataFrame = self.df[[time_column, price_column]].rename(columns = rename_dict)
        return self

    def get_dataframe(self) -> pd.DataFrame:  
        return self.df
    

class ColumnNotSetException(Exception):
    def __init__(self, lack_column:List[str]):
        message = "Column not set : " + ",".join(lack_column)
        super().__init__(message)
