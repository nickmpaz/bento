import yaml
import pathlib
import sys
from .. import settings

def parse_config():
   try:
      cwd = pathlib.Path.cwd()
      config_name = settings.config_name
      config_abs_path = pathlib.PurePath.joinpath(cwd, config_name)
      with open(config_abs_path) as f:
         config = yaml.load(f, Loader=yaml.FullLoader) 
   except FileNotFoundError:
      print(settings.config_not_found_message)
      sys.exit()
    
   print(config)
