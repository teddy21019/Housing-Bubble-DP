from abc import ABC, abstractmethod
from typing import Callable, Any
import pandas as pd
import statsmodels.api as sm
from src.typing_alias import DataPipe


class FilterLayer(ABC):


    @property
    @abstractmethod
    def filter_func(self) -> DataPipe:
        ...


class HPFilter(FilterLayer):
    def __init__(self, llambda: int = 100, freq:str = 'Y') -> None:
        self._lambda = llambda
        self.freq = freq

    @property
    def filter_func(self) -> DataPipe:

        def hp(dat: pd.DataFrame):
            
            times = list(dat['time']) 
            start_time = times[0] 
            end_time = times[-1] 
            t = pd.period_range(start_time, end_time, freq=self.freq) 
            dat.set_index(t, inplace=True) 
            
            cycle, trend = sm.tsa.filters.hpfilter(dat["price"], self._lambda)  ## lambda is set as 100 for annual
            return_data = dat[["price"]] 
            return_data['time'] = dat['time']
            return_data['cycle'] = cycle
            return_data['trend'] = trend 
            
            return return_data

        return hp