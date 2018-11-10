import pandas as pd
import numpy as np

from textblob import TextBlob

import warnings
warnings.filterwarnings('ignore')

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
#from plotly.offline import init_notebook_mode, iplot
#import plotly.figure_factory as ff
#init_notebook_mode(connected=True)
#plt.style.use('fivethirtyeight')
#%matplotlib inline


curr_dir = 'C:\Users\kishore vavilapalli\Downloads\ nyt-comments'
comments = pd.read_csv(curr_dir + 'CommentsApril2018.csv')
articles = pd.read_csv(curr_dir + 'ArticlesApril2018.csv')


def print_largest_values(s, n=5):
    s = sorted(s.unique())
    for v in s[-1:-(n + 1):-1]:
        print(v)
    print()


def print_smallest_values(s, n=5):
    s = sorted(s.unique())
    for v in s[:n]:
        print(v)
    print()

comments.sample(5)



