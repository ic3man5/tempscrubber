# tempscrubber
Python script to remove files in a directory based on created time.

# How to use

Running this script/executable will look for configuration YAML files located in your home path under `.tempscrubber`. If this directory doesn't exist it will create it and place an example YAML file there.

`~/.tempscrubber/temp_files.yaml` Example:

```yaml
# This configuration file needs to be placed in %HOMEPATH%\.temp_scrubber\temp_files.yaml (~/.temp_scrubber/temp_files.yaml on linux)
# H = Hours
# D = Days
# W = Weeks
# M = Months (30 days assumed always)
# Y = Years

5MinuteLocation:
  location: C:\share\5M
  duration: 5

24HoursLocation:
  location: C:\share\24hr
  duration: 24H

3DayLocation:
  location: C:\share\3Days
  duration: 3D

3MonthLocation:
  location: C:\share\3Months
  duration: 3M

1YearLocation:
  location: C:\share\1Year
  duration: 1Y
```

Running this will produce the following output:

```
Iterating through "C:\share\5M"...
Iterating through "C:\share\24hr"...
Iterating through "C:\share\3Days"...
Iterating through "C:\share\3Months"...
Iterating through "C:\share\1Year"...
```


License
---

MIT
```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
