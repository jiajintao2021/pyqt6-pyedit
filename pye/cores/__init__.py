import os
import typing

from settings import CONFIG_DIRPATH
from pye.cores.models import SettingsModel


__all__ = [
    'Settings',

    'CustomSettings',
]

_settings_filename = '.settings.json'

_settings_model: typing.Optional[SettingsModel] = None
_settings_filepath = os.path.join(CONFIG_DIRPATH, _settings_filename)
if not os.path.isfile(_settings_filepath):
    with open(_settings_filepath, mode='w', encoding='utf8') as f:
        _settings_model = SettingsModel()
        settings_json = _settings_model.json(indent=4)
        f.write(settings_json)

_settings_model: typing.Optional[SettingsModel] = SettingsModel.parse_file(_settings_filepath)


class SettingsProject:
    settings: SettingsModel

    def project_update(self, project_path, is_right=False):
        if is_right:
            self.settings.project.append(project_path)
        else:
            self.settings.project.insert(0, project_path)


class Settings(SettingsProject):
    settings_filepath = _settings_filepath
    settings_last: typing.Optional[typing.Dict[str, typing.Any]] = {}
    settings: SettingsModel = _settings_model

    def update(self, **kwargs):
        for key, new_value in kwargs.items():
            if not hasattr(self.settings, key):
                raise KeyError(f'NotFound Key:{key} In SettingsModel')

            old_value = getattr(self.settings, key)
            if old_value == new_value:
                continue
            self.settings_last[key] = old_value

            func_name = key + '_' + self.update.__name__
            if hasattr(self, func_name):
                h = getattr(self, func_name)
                h(new_value)
            else:
                setattr(self.settings, key, new_value)

    def save(self):
        with open(self.settings_filepath, mode='w', encoding='utf8',) as f:
            json_content = self.settings.json(indent=4)
            f.write(json_content)

    def clear_settings_last(self):
        self.settings_last.clear()

    def rollback(self):
        for key, old_value in self.settings_last.items():
            setattr(self.settings, key, old_value)


class CustomSettings(Settings):
    pass


Settings: Settings = Settings()
