from abc import ABC, abstractmethod
import pandas as pd
class FilterLayer(ABC):

    @abstractmethod
    def validate(self) -> None:
        ...

    @abstractmethod
    def get_data(self, df:pd.DataFrame) -> pd.DataFrame:
        ...


class HPFilter(FilterLayer):
    pass