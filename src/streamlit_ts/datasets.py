import pandas as pd
import numpy as np

def dfTS_gen(nsize, ncat, ncols, start="2018-01-01", freq="D"):
    # generate data
    list_df = []
    for i in range(ncat):
        df = pd.DataFrame()
        df["date"] = pd.date_range(start, periods=nsize, freq=freq)
        for j in range(ncols):
            df[f"col{j}"] = np.linspace(0, nsize-1, nsize)

        df.set_index("date", inplace=True)
        list_df.append(df)

    return pd.concat(list_df).sort_index()
