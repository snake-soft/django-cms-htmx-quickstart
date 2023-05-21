import os
from pathlib import Path


file_path = Path(__file__).parent.parent.joinpath('HASH')
if file_path.is_file():
    with open(file_path, 'r') as file:
        git_commit_id = file.read()
else:
    git_commit_id = 'Unbekannt'


file_path = Path(__file__).parent.parent.joinpath('VERSION')
if file_path.is_file():
    with open(file_path, 'r') as file:
        __version__ = file.read()
else:
    __version__ = 'Unbekannt'
