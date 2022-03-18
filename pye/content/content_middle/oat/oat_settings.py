import os
import typing

from pye.cores import CustomSettings
from pydantic import BaseModel

from settings import BASE_DIR


__all__ = [
    'OatSettingDefaultModel',
    'oat_setting_model_default',

    'OatSettingDefault',
    'oat_setting_default',
]


class OatSettingDefaultModel(BaseModel):
    oat_basedir: str = BASE_DIR
    oat_data_dirname: str = 'oat_data'
    oat_data_dirpath: str = os.path.join(oat_basedir, oat_data_dirname)

    oat_setting_filename: str = 'oat_settings.json'
    oat_setting_filepath: str = os.path.join(oat_data_dirpath, oat_setting_filename)

    event_filename: str = '.event.oat'
    event_dirpath: str = oat_data_dirpath
    event_filepath: str = os.path.join(event_dirpath, event_filename)


oat_setting_model: typing.Optional[OatSettingDefaultModel] = None
oat_setting_model_default = OatSettingDefaultModel()

if not os.path.isdir(oat_setting_model_default.oat_data_dirpath):
    os.mkdir(oat_setting_model_default.oat_data_dirpath)

if not os.path.isfile(oat_setting_model_default.event_filepath):
    with open(oat_setting_model_default.event_filepath, mode='wb') as f:
        f.write(b'')

if not os.path.isfile(oat_setting_model_default.oat_setting_filepath):
    with open(oat_setting_model_default.oat_setting_filepath, mode='w', encoding='utf8',) as f:
        f.write(
            oat_setting_model_default.json(
                indent=4,
                exclude={'oat_basedir', 'oat_data_dir', 'oat_data_dirpath'}
            )
        )

oat_setting_model = OatSettingDefaultModel.parse_file(oat_setting_model_default.oat_setting_filepath)


class OatSettingDefault(CustomSettings):
    settings_filepath = oat_setting_model.oat_setting_filepath
    settings = oat_setting_model


oat_setting_default = OatSettingDefault()
