from typing import List, Dict, Union
import pathlib 
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'config.yaml'

def get_config(doc_name: List[str] = ['all']) -> Dict:
    config: Dict = dict()

    with open(config_path) as f:
        for document in yaml.safe_load_all(f):
            if document and (doc_name == ['all'] or list(document.keys()) == doc_name):
                config.update(document)

    return config

def set_config(document_name: str, key: str, value: Union[str, int]) -> None:
    update_config: Dict = dict()
    
    with open(config_path, 'r') as f:
        for document in yaml.safe_load_all(f):
            if document:
                for k, v in document.items():
                    update_config[k] = v

    if update_config.get(document_name, False):
        update_config[document_name][key] = value
    else:
        update_config[document_name] = {key: value}

    with open(config_path, 'w') as f:
        for data in update_config:
            f.write('---\n')
            yaml.dump({data: config[data]}, f)

config = get_config()
set_config('client_telegram', 'app_version', "version")

CONFIG_CLIENT_TELEGRAM = config['client_telegram']
CONFIG_SERVER = config['server']