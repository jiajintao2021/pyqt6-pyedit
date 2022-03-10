import os
import sys

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

CONFIG_DIRNAME = 'configs'
CONFIG_DIRPATH = os.path.join(BASE_DIR, CONFIG_DIRNAME)
if not os.path.isdir(CONFIG_DIRPATH):
    os.mkdir(CONFIG_DIRPATH)

TEMP_DIRNAME = 'temp'
TEMP_DIRPATH = os.path.join(BASE_DIR, TEMP_DIRNAME)
if not os.path.isdir(TEMP_DIRPATH):
    os.mkdir(TEMP_DIRPATH)

STATIC_DIRNAME = 'statics'
STATIC_DIRPATH = os.path.join(BASE_DIR, STATIC_DIRNAME)

QSS_DIRNAME = 'qss'
QSS_DIRPATH = os.path.join(STATIC_DIRPATH, QSS_DIRNAME)

ICONS_DIRNAME = 'icons'
ICONS_DIRPATH = os.path.join(STATIC_DIRPATH, ICONS_DIRNAME)
