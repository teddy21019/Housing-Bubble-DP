from functools import partial
from matplotlib import pyplot as plt

from src.JST.preprocessing import createRealPrice
from src.df_preprocessor import JSTDataFrameLoader
from src.bubble_detector import BubbleDetector
from src.presenter import GraphBubble, ListBubble
from src.Filter import HPFilter


jst_file_path = "data/JSTdatasetR5.xlsx"


def main():

    fig, ax = plt.subplots(1, 1, figsize=(5, 7))
    country_code = 'SWE'
    create_real_gdp_fn = partial(createRealPrice, nomvar='hpnom')

    df_loader = JSTDataFrameLoader(
        data_path=jst_file_path,
        country=country_code)
    
    df_loader.pre_transform(create_real_gdp_fn)       \
            .set_time_price(time_column='year', price_column='real_hpnom')

    trend_filter = HPFilter(llambda = 100)

    bubble = BubbleDetector(df_loader.get_dataframe(), trend_filter)
    
    presenter = GraphBubble(bubble, axis=ax, start_index=1985, end_index=1995)\
        .set_axis_name(x='year', y='price')\
        .set_title("Housing price for USA, 2001-2011")
    # presenter = ListBubble(bubble)

    presenter.present()

    plt.show()









if __name__ == "__main__":
    main()