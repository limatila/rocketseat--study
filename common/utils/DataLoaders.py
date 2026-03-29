import json

import pandas as pd

from common.config.core import PROJECT_ROOT


def load_json_to_dict(file_name: str, parent_path: str = "./data", exclude_keys: list[str] = []) -> dict:
    """ Load a dict from a JSON saved file.
    
    :param file_name: "file_name.json to load"
    :type file_name: str
    :param parent_path: "parent directory where the file is located"
    :type parent_path: str
    :param exclude_keys: "list of keys to exclude"
    :type exclude_keys: list[str]
    :return: Description
    :rtype: Obtained dict
    """ 
    
    file_name = file_name + ".json"
    final_path = PROJECT_ROOT / parent_path / file_name

    if final_path.is_file() == False:
        raise FileNotFoundError(f"Arquivo {final_path.__str__().replace(PROJECT_ROOT.__str__(), '')} não existe.")
    
    with open(final_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for key in exclude_keys:
        if key in data:
            data.pop(key)
    
    return data


def load_csv_to_dataframe(file_name: str, parent_path: str = "./data", exclude_keys: list[str] = [], **kwargs_pd) -> 'pd.DataFrame':
    """ Load a DataFrame from a CSV saved file.
    
    :param file_name: "file_name.csv to load"
    :type file_name: str
    :param parent_path: "parent directory where the file is located"
    :type parent_path: str
    :param exclude_keys: "list of column names to exclude"
    :type exclude_keys: list[str]
    :return: Description
    :rtype: Obtained DataFrame
    """ 

    file_name = file_name + ".csv"
    final_path = PROJECT_ROOT / parent_path / file_name
    
    dataframe = pd.read_csv(final_path, **kwargs_pd)

    dataframe = dataframe.drop(columns=exclude_keys)
    
    return dataframe