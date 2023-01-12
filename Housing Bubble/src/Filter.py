from abc import ABC, abstractmethod
from typing import Callable, Any
import pandas as pd
class FilterLayer(ABC):


    @abstractmethod
    def get_filter_func(self) -> Callable[... , pd.DataFrame]:
        ...


class HPFilter(FilterLayer):
    pass