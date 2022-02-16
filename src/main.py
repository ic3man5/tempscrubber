import pathlib
from config.manager import ConfigManager
from scrubber import Scrubber, TimeInfo

if __name__ == "__main__":
    config_manager = ConfigManager()
    config = config_manager.load('temp_files.yaml')
    for name, values in config.items():
        print(f"""Iterating through "{values['location']}"...""")
        path = pathlib.Path(values['location'])
        for f in path.glob('*'):
            scrubber = Scrubber(str(f), TimeInfo(values['duration']))
            scrubber.scrub()
