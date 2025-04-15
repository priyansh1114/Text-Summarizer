import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from box import config_box
from pathlib import Path
from typing import Any, Dict, List
from ensure import ensure_annotations 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> config_box:
    """
    Reads a YAML file and returns its content as a Box object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        config_box: Content of the YAML file as a Box object.
    """
    try:
        with open(path_to_yaml, 'r', encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return config_box(content)
    except FileNotFoundError as e:
        logger.error(f"File not found: {path_to_yaml}")
        raise e
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    

@ensure_annotations
def create_directories(dirs: List[str]):
    """
    Creates directories if they do not exist.

    Args:
        dirs (List[str]): List of directory paths to create.
    """
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
        logger.info(f"Created directory: {dir}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file or directory.

    Args:
        path (Path): Path to the file or directory.

    Returns:
        str: Size of the file or directory in bytes.
    """
    if os.path.isfile(path):
        return f"File size: {os.path.getsize(path)} bytes"
    elif os.path.isdir(path):
        total_size = sum(os.path.getsize(f) for f in os.listdir(path) if os.path.isfile(f))
        return f"Directory size: {total_size} bytes"
    else:
        return "Path does not exist"