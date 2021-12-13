import json
import src.utils.constants as C

with open(C.CONFIG_PATH, 'r') as file_:
    TRANSFORMER_CONFIG = json.load(file_)
