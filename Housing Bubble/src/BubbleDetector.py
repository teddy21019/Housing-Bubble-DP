
from src.DFLoader import DFLoader
import pandas as pd
from src.Filter import FilterLayer


class BubbleDetector:

    def __init__(self, 
                df_loader: DFLoader,
                filter: FilterLayer
    ) -> None:
        self.df_loader = df_loader
        self.filter = filter

        
        self.df_loader.validated()
        


