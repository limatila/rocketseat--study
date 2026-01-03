import json

from pathlib import Path

from common.config.core import PROJECT_ROOT


def load_json_to_dict(file_name: str, parent_path: str = "./data") -> dict:
    """ Load a dict from a JSON saved file.
    
    :param file_name: "file_name.json to load"
    :type file_name: str
    :param parent_path: "parent directory where the file is located"
    :type parent_path: str
    :return: Description
    :rtype: Obtained dict
    """ 
    file_name = file_name + ".json"
    final_path = PROJECT_ROOT / parent_path / file_name
    
    with open(final_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

def save_dict_to_json(data_to_dump: dict, file_name: str, parent_path: str = "./data", overwrite: bool = False) -> Path:
    """ Save a dict in a JSON stored file.

    :param data_to_dump: "dict to be saved"
    :type data_to_dump: dict

    :param file_name: "file_name.json to save"
    :type file_name: str
    :param parent_path: "parent directory where the file is located"
    :type parent_path: str
    :return: The path where the file was saved
    :rtype: Path
    """
    file_name = file_name + ".json"
    final_path = PROJECT_ROOT / parent_path / file_name

    with open(final_path, 'r') as file:
        if not overwrite and len(file.readlines()) > 0:
            raise FileExistsError(
                f"The file {final_path} already contains content. \nTo overwrite it, you can set the 'overwrite' parameter to True."
            )
    
    with open(final_path, 'w', encoding='utf-8') as file:
        json.dump(data_to_dump, file, indent=4)

    return final_path