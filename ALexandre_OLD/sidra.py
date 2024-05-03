import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html
import sidrapy

st.set_page_config(
    page_title="Use Pygwalker with Streamlit",
    layout="wide"
)

st.title("PyGWalker with Streamlit")

# Initialize pygwalker communication
init_streamlit_comm()

# When using `use_kernel_calc=True`, you should cache your pygwalker html, if you don't want your memory to explode
@st.cache(allow_output_mutation=True)
def get_pyg_html(df: pd.DataFrame) -> str:
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    # If you want to use feature of saving chart config, set `debug=True`
    html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
    return html

@st.cache(allow_output_mutation=True)
def get_df() -> pd.DataFrame:
    pib_sa_raw = sidrapy.get_table(table_code= "1621",
                                territorial_level = "1",
                                ibge_territorial_code = "all",
                                period = "all",
                                classification = "11255/90707")
    df = pd.DataFrame(pib_sa_raw)
    return df

df = get_df()

components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)