from abc import ABC, abstractmethod
import pandas as pd
from src.DataLoader import DataLoader
from typing import List


class DFLoader(ABC):
    """
        Abstract class for pd.Dataframe loader
    """
    data_loader : DataLoader

    @abstractmethod
    def get_dataframe(self) -> pd.DataFrame:
        """
        Returns the dataframe associated with the given data_loader
        """
        ...

    @abstractmethod
    def set_time_price(self, time_column:str, price_column:str):
       pass 


    @abstractmethod
    def validated(self):
        pass



class JST_DFLoader(DFLoader):
    """
    Reads an JST macroeconomic database and filters the 
    information based on the country and extracts the time and price column
    """
    def __init__(self, 
                data_loader : DataLoader, 
                country: str) -> None:
        """
            The constructor of a Dataframe loader specifically for 
            the JST database.


            Parameters
            ==========
            data_loader : DataLoader
                The DataLoader class that loads the JST database.
                This functionality is extracted in case the formot of the 
                JST database is altered in the future for some reason. 
            
            country: str 
                The country to filter. Comes in the case of a country code.

            price_column: str
                The column of the price that is wanted. 
                Note that one might need to do some transformation, i.e. deflation or 
                getting the percentage change before assigning. 
        """
        self.data_loader = data_loader
        self.df = self.data_loader.read_file()
        self.df = self.df[self.df['iso'] == country]

        self.column_changed = False


    @abstractmethod
    def pre_transform(self):
        pass 

    def set_time_price(self, time_column:str, price_column:str):
        rename_dict = {
            time_column:"time",
            price_column:"price"
        }

        self.df:pd.DataFrame = self.df[[time_column, price_column]].rename(rename_dict)
        self.column_changed = True
        return self

    def get_dataframe(self) -> pd.DataFrame:  

        if not self.column_changed:
            raise ColumnNotSetException(
                [col_name for col_name in ["time", "price"] 
                    if col_name not in self.df.columns
                ]
            )
        

        return self.df


class ColumnNotSetException(Exception):
    def __init__(self, lack_column:List[str]):
        message = "Column not set : " + ",".join(lack_column)
        super().__init__(message)
