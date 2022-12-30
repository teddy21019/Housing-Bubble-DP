# Housing-Bubble-DP
A housing bubble detection example of using some design patterns to restructure the code

The initial code for detecting housing bubble can be found in my medium post:

[Housing Bubbles in History — A Detection Using Python](https://medium.com/@ted21019/housing-bubbles-in-history-a-detection-using-python-c959261c5b35)

[Initial code](https://gist.github.com/teddy21019/96454b50ac361476d6eafa89cb5635fb#file-housing_bubble-ipynb)
## Problem with the original code
1. Hard to extend to different data source

The original code aims to handle the JST database, and thus include handling country filtering and real-price transforming. 
These might not be the case for other data sources that we too want to detect some sort of bubbles in the time series.

2. Hard to implement different filtering algorithm

The original code implements an HP filter as a tool to detrend. There are critisisms regarding using HP filter, 
but for our code it is not that obvious how it can be easily interchaging the method. 

3. Output is tied to visualizing via `matplotlib`

After the bubble detection algorithm is run, the original code simply plots the result. 
It is nice if there exists some freedom to choose the desired format of presentation, perhaps a listing of years instead of graphs.
The original code does not easily allow this dependancy. 

## Solution

The solution is to use design patterns. Specifically, the "factory" pattern for creating objects and the "strategy pattern" for implementing a specific algorithm. 
