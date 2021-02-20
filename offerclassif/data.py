import json 
import pandas as pd

def load_json(file:str):
    """Json loading function

    Args:
        file (str): Path to json

    Returns:
        list/dict: Loadded json object.
    """
    with open(file) as f:
        data = json.load(f)
    print(f'{len(data)} items loaded from {file}.')
    
    return data


def get_df(offers:list, thesaurus:list=None) -> pd.DataFrame:
    """Tranform offers loads from json file into DataFrame

    Args:
        offers (list): Offers list loads from json file
        thesaurus (list, optional): Job thesorus load from json file. Defaults to None.

    Returns:
        pandas.DataFrame: Offers
    """
    df = pd.DataFrame([{
        'id': i.get('employments',[{}])[0].get('employment_id', None),
        'description': i['description'],
        'title': i['title'],
        'text': i['title'] + '. ' + i['description']
    } for i in offers])
        
    if thesaurus:
        df = pd.merge(pd.DataFrame(thesaurus), df, how='right')

    return df

