import json 

def load_json(file):
    """Json loading function

    Args:
        file (str): Path to json

    Returns:
        list/dict: Loadded json object.
    """
    with open(file) as f:
        data = json.load(f)
    print(f'{len(data)} loaded from {file}.')
    
    return data