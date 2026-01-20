# save images, plots

import json
from pathlib import Path

from common.config.core import PROJECT_ROOT


def save_dict_to_json(
    data_to_dump: dict | list[dict], file_name: str, parent_path: str = "./data/output", overwrite: bool = False
) -> Path:
    """ Save a dict in a JSON stored file.

    :param data_to_dump: data to be saved
    :type data_to_dump: dict | list[dict] or any serializable to JSON

    :param file_name: file_name.json to save
    :type file_name: str
    :param parent_path: parent directory where the file is located
    :type parent_path: str
    :return: The path where the file was saved
    :rtype: Path
    """
    file_name = file_name + ".out.json"
    final_path = PROJECT_ROOT / parent_path / file_name

    final_path.parent.mkdir(parents=True, exist_ok=True)
    final_path.touch(exist_ok=True)

    with open(final_path, 'r') as file:
        if not overwrite and len(file.readlines()) > 0:
            raise FileExistsError(
                f"The file {final_path} already contains content. \nTo overwrite it, you can set the 'overwrite' parameter to True."
            )
    
    with open(final_path, 'w', encoding='utf-8') as file:
        json.dump(data_to_dump, file, indent=4)

    return final_path