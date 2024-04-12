from streamlit_ts.datasets import dfTS_gen

def test_data():
    """It creates the dataframe correctly."""
    data = dfTS_gen(nsize=100, ncat=1, ncols=1, start="2020-01-01")
    assert len(data) == 100
