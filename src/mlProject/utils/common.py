import os
from box.exceptions import BoxValueError
import yaml
import json
from mlProject import logger
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''Read yaml file'''
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose= True):
    '''Create list of directories'''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    '''save json data'''
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    '''load json file data'''
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from {path}")
    return content


@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    '''load the binary data'''
    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    '''Get size in KB'''
    size_in_kb = round(os.path.getsize(path))
    return f"~ {size_in_kb} KB"


