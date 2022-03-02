from pye.core.dir import get_dirtree
from settings import BASE_DIR

data = get_dirtree(BASE_DIR, ignore_str=['build', 'venv', '.git', '.idea', '__pycache__'])
print(data)
