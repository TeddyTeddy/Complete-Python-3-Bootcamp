import math   # which math? our custom one or non-builtin standard library's math? The former
print(dir(math))
import time
print(dir(time))  # built-in time module gets called, not our custom time.py
print(time.tzname)
