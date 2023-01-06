from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd
class DataLoader(ABC):

    @abstractmethod
    def read_file(self):
        ...


class JST_DataLoader(DataLoader):

    def __init__(self, file_path:Path):
        self.file_path = file_path
    
    def read_file(self) -> pd.DataFrame:
        """
        Default format for reading the JST dataset is excel file.
        """
        return pd.read_excel(self.file_path, 
                            engine="openpyxl",
                            sheet_name="Data")