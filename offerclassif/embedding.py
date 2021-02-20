
import spacy
import numpy as np

nlp = spacy.load("fr_core_news_md")

def get_vectors(serie):

    out = []
    for text in serie:
        assert isinstance(text, str)
        doc = nlp(text)
        vect = [t.vector for t in doc if not t.is_stop and not t.is_punct and t.pos_ in ["NOUN", "PROPN", "ADJ", "X"] and len(t)>2]
        vect = np.mean(vect, axis = 0)
        out.append(vect)
        
    return np.asarray(out)
