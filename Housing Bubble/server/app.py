import sys, os
sys.path.append(os.path.abspath(".."))

import streamlit as st 
import matplotlib.pyplot as plt
from functools import partial
from src.Filter import HPFilter
from src.JST.preprocessing import createRealPrice
from src.JST.file_loader import jst_dataset_loader
from src.df_preprocessor import JSTDataFrameLoader
from src.bubble_detector import BubbleDetector
from src.presenter import PlotlyBubble, GraphBubble 
from src.Filter import HPFilter
st.set_page_config(layout="wide")

jst_dataset_loader = st.cache_data(jst_dataset_loader)
jst_file_path = "../data/JSTdatasetR5.xlsx"
jst_df = jst_dataset_loader(jst_file_path)

left_col, right_col = st.columns(2)
with left_col:
    country_code = st.selectbox('Country: ', jst_df['iso'].unique() )
    start, end = st.slider('Year range: ' , min_value=1875, max_value=2017, value=(1950, 2000))
    llambda = st.slider('Lambda value:', min_value=10, max_value=300, value=200)

create_real_gdp_fn = partial(createRealPrice, nomvar='hpnom')

df_loader = JSTDataFrameLoader(
    jst_df=jst_df,
    country=country_code)

df_loader.pre_transform(create_real_gdp_fn)       \
.set_time_price(time_column='year', price_column='real_hpnom')

trend_filter = HPFilter(llambda = llambda)

bubble = BubbleDetector(df_loader.get_dataframe().reset_index(drop=True), trend_filter)


left_col.dataframe(bubble.bubble_df)


# presenter = PlotlyBubble(bubble, start_index=1985, end_index=1995)\
    # .set_axis_name(x='year', y='price')\
    # .set_title("Housing price for USA, 2001-2011")
# 


fig, ax = plt.subplots(1, 1, figsize=(7, 5))

presenter = GraphBubble(bubble=bubble, start_index=start, end_index=end, axis=ax)\
    .set_axis_name(x='year', y='price')\
    .set_title(f"Housing price for {country_code}, {start}-{end}")
ax = presenter.present()

with right_col:
    fig

# st.plotly_chart(
#     fig, 
#     theme="streamlit", use_container_width=True)