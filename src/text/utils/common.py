import os
from venv import logger 
from box.exceptions import BoxValueError 
import yaml 
from text.logging import logger 
from ensure import ensure_annotations 
from box import  ConfigBox 
from pathlib import Path 
from typing import Any



@ensure_annotations 
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns it as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the yaml file."""
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose= True):
    """Creates directories if they don't exist.
    
    Args:
        path_to_directories (list): List of paths to directories to create.
        verbose (bool): Whether to log the creation of directories."""
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file or directory in KB, MB, or GB.

    Args:
        path (Path): Path to the file or directory.

    Returns:
        str: Size of the file or directory in a human-readable format.
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

