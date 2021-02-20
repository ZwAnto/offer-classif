import pprint

import plotly.express as px
from plotly.subplots import make_subplots


def plot_tsne(tsne, df):
    
    fig1 = px.scatter(x=tsne[:,0], y=tsne[:,1], color=df.sector_internal_label)
    fig2 = px.scatter(x=tsne[:,0], y=tsne[:,1], color=df.internal_label)

    fig = make_subplots(rows=1, cols=2)

    _ = [fig.add_trace(t, row=1, col=1) for t in fig1['data']]
    _ = [fig.add_trace(t, row=1, col=2) for t in fig2['data']]


    fig.update_layout(width=1000, height=500, title='Violin per feature', title_x=0.5)
    fig.update_xaxes(matches=None)
    fig.update_yaxes(matches=None)
    fig.show()



def topNoob(model, classes, n=3):
    
    topn_pred = model.oob_decision_function_.argsort(axis=1)[:,-n:]
    topn_pred = [[ model.classes_[j] for j in i] for i in topn_pred]

    return sum([i in j for i,j in zip(classes, topn_pred)])/len(classes)



class P(pprint.PrettyPrinter):
  def _format(self, object, *args, **kwargs):
    if isinstance(object, str):
      if len(object) > 80:
        object = object[:80] + '...'
    return pprint.PrettyPrinter._format(self, object, *args, **kwargs)


def format_prediction(samples, pred, thesaurus):

    for i,j in zip(samples, pred):

        jobs = filter(lambda x: x['internal_label'] == j, thesaurus)
        i.update({"employments": [{"employment_id": i['id']} for i in jobs]})
