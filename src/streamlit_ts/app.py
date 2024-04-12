import streamlit as st
import pandas as pd

from streamlit_ts.datasets import dfTS_gen


dataf = dfTS_gen(nsize=100, ncat=1, ncols=3, start="2020-01-01")

def main(data):
    """It runs the app."""

    st.write("""
    # My first app
    Hello *world!*
    """)
    st.line_chart(data)


if __name__ == "__main__":
    main(data=dataf)