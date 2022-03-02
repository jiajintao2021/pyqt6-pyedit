import os
import sys

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

CONFIG_DIRNAME = 'configs'
CONFIG_DIRPATH = os.path.join(BASE_DIR, CONFIG_DIRNAME)
if os.path.isdir(CONFIG_DIRPATH):
    os.mkdir(CONFIG_DIRPATH)
