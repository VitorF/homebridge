#!/usr/local/bin/python3

# With support from
# https://github.com/mjg59/python-temescal
# https://www.reddit.com/r/homeassistant/comments/yey98p/need_help_for_using_pythontemescal_to_connect_lg/


import json
import temescal
import time

def speaker_callback(response):
    if(response["msg"]!="PLAY_INFO"):
        print(json.dumps(response))

try:
    speaker = temescal.temescal("10.1.4.22", callback=speaker_callback)
except OSError as err:
    print(err)
except:
    print("Unknown error")

speaker.get_func()

time.sleep(3)