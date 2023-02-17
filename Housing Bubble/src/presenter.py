from __future__ import annotations

from abc import ABC, abstractmethod
from src.bubble_detector import BubbleDetector
import matplotlib.pyplot as plt

class BubblePresenter(ABC):
    def __init__(self, bubble: BubbleDetector): 
        self.bubble = bubble
    
    @abstractmethod
    def present(self):
        ...
    

class GraphBubble(BubblePresenter):

    def __init__(self,  bubble: BubbleDetector, 
                        axis:plt.Axes, 
                        start_index, end_index
                        ):
        super().__init__(bubble)
        self.axis = axis
        self.start_index = str(start_index)
        self.end_index = str(end_index)
    
    def set_title(self, title: str) -> GraphBubble:
        self.plot_title = title
        self.axis.set_title(title)
        return self

    def set_axis_name(self, x:str, y:str) -> GraphBubble:
        self.x_name = x
        self.y_name = y
        return self

    def present(self):
        plot_df = self.bubble.bubble_df[self.start_index : self.end_index]

        time_ax = plot_df['time']
        ax = self.axis
        ax.plot(time_ax, plot_df['price'])     # plot pd.Series
        ax.fill_between(time_ax, plot_df['upper'], plot_df['lower'], alpha = 0.2)   # plot the band
        
        # get the episodes from boolean mask
        bubble_period = plot_df[
            plot_df["is_bubble"]
        ] 
        
        bubble_year = bubble_period['time']
        bubble_value = bubble_period['price']
        
        ax.scatter(bubble_year, bubble_value, color='black') 
        
        # plot the points that is detected
        for x,y in zip(bubble_year, bubble_value): 
            ax.annotate(x,
                    (x,y),
                    textcoords="offset points", 
                    xytext=(0,-20),
                    ha='center') 

        return ax


class ListBubble(BubblePresenter):
    def present(self):
        df = self.bubble.bubble_df
        bubble_period = df[df.is_bubble == True]

        period_strings = [str(t) for t in bubble_period['time']]
        return("Bubble period:" + ', '.join(period_strings))

class APIBubble(BubblePresenter):
    def present(self):
        df_json = self.bubble.bubble_df.to_json(orient='index')
        return df_json
        