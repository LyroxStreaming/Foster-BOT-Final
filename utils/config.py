import json
import os

with open("info.json", "r") as f:
    DATA = json.load(f)

OWNER_IDS = DATA["996060367585300490"]
EXTENSIONS = DATA["EXTENSIONS"]
No_Prefix = DATA["np"]
