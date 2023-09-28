import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logging
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''
    Reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Returns:
        ConfigBox: Configbox type

    '''

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    Creates list of directories

    Args:
        path_to_directories (list): list containing path of directories
        ignore_log (bool, optional): ignore if multiple dirs to be created. Default is False.

    '''

    for path in path_to_directories:            
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")


def save_json(path: Path, data: dict):
    '''
    Saves data from json

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    '''

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

        logging.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''
    load json file data
     Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    '''
    with open(path) as f:
        content = json.load(f)

        logging.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    '''
    Save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binray file
    '''
    data = joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    '''
    get size in KB

    Args:
        path (Path): path to the file

    Returns:
        str: size in KB
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):

    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):

    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())