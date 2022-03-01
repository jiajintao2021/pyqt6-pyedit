from pye1.window import PyE_Menu_Project_Open
from pye_scripts.events_sys.menu_events import open_project_e

PyE_Menu_Project_Open.triggered.disconnect()
PyE_Menu_Project_Open.triggered.connect = open_project_e
