import numpy as np
import pandas as pd

if __name__ == '__main__':
    s = pd.Series([1, np.nan, 3, 4, 5, None])
    print(s.mean())
    print(s.isnull())