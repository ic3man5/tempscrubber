import pathlib
from dataclasses import dataclass
import re
import datetime
import shutil

@dataclass
class TimeInfo(object):
    value: str

    def _convert_value_to_minutes(self):
        """Converts the value to minutes"""
        # If we have a straight integer already, we assume its minutes.
        if isinstance(self.value, int):
            return self.value
        conversions = {
            'H': 60,
            'D': 60*24,
            'W': 60*24*7,
            'M': 60*24*7*30,
            'Y': 60*24*365,
        }
        regex = re.compile(r"[A-Z]$")
        value = re.sub(r'[aA-zZ]+', '', self.value)
        matches = regex.findall(self.value)
        value = int(value)
        letter = matches[0]
        if not letter in conversions:
            raise RuntimeError(f'''"{self.value}" doesn't have a valid letter type''')
        return value * conversions[letter]

    def seconds(self):
        return self._convert_value_to_minutes() * 60
    
    def minutes(self):
        return self._convert_value_to_minutes()
    
    def hours(self):
        return self._convert_value_to_minutes() / 60

    def days(self):
        return self._convert_value_to_minutes() / (60*24)
    
    def years(self):
        return self._convert_value_to_minutes() / (60*24*365)


class Scrubber(object):
    def __init__(self, fname, time_info: TimeInfo):
        self.fname = fname
        self.time_info = time_info
        self.path = pathlib.Path(fname)
        if not self.path.exists():
            raise FileNotFoundError(str(self.path))

    def scrub(self):
        current = datetime.datetime.now()
        f_time = datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        elapsed = current - f_time
        max_allowed = datetime.timedelta(minutes=self.time_info.minutes())
        if elapsed >= max_allowed:
            print(f'''Removing "{str(self.path)}"...''')
            if self.path.is_file():
                self.path.unlink()
            elif self.path.is_dir():
                shutil.rmtree(str(self.path))
            else:
                raise RuntimeError("Unsupported file type!")