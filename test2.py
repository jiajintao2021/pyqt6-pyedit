import json
import os

from pye.cores import _settings_filename
from settings import CONFIG_DIRPATH

settings_filepath = os.path.join(CONFIG_DIRPATH, _settings_filename())
with open(settings_filepath, mode='r', encoding='utf8') as f:
    j = json.loads(f.read())
    print(j, type(j))
    # settings_model: typing.Optional[SettingsModel] = SettingsModel(**json.load(f))


s = "{\n     \"project\": [1,2]}"
data = json.loads(s)
print(data, type(data))
