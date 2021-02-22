
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from sklearn.ensemble import ExtraTreesClassifier


def plot_tsne(tsne:np.array, df:pd.DataFrame):
    """Function to plot TSNE

    Args:
        tsne (np.array): [description]
        df (pd.DataFrame): [description]
    """
    fig1 = px.scatter(x=tsne[:,0], y=tsne[:,1], color=df.sector_internal_label)
    fig2 = px.scatter(x=tsne[:,0], y=tsne[:,1], color=df.internal_label)

    fig = make_subplots(rows=1, cols=2)

    _ = [fig.add_trace(t, row=1, col=1) for t in fig1['data']]
    _ = [fig.add_trace(t, row=1, col=2) for t in fig2['data']]


    fig.update_layout(width=1000, height=500, title_x=0.5)
    fig.update_xaxes(matches=None)
    fig.update_yaxes(matches=None)
    fig.show()


def topNoob(model:ExtraTreesClassifier, classes:list, n:int=3) -> float:
    """Compute top N accuracy using OOB proba

    Args:
        model (ExtraTreesClassifier): Sklearn ExtraTreesClassifier 
        classes (list): Real labels/classes
        n (int, optional): Number of prediction to consider (top n). Defaults to 3.

    Returns:
        float: Accuracy
    """
    topn_pred = model.oob_decision_function_.argsort(axis=1)[:,-n:]
    topn_pred = [[ model.classes_[j] for j in i] for i in topn_pred]

    return sum([i in j for i,j in zip(classes, topn_pred)])/len(classes)
