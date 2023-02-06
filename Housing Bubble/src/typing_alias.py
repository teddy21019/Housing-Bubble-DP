
from typing import Callable

import pandas as pd


DataPipe = Callable[[pd.DataFrame], pd.DataFrame]