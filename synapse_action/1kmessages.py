import requests
import hmac, hashlib 

import time
import random
import string

from get_access_code import acquire_token

"""
Example:
"2026-02-08T09:02:09.310Z": {
    "method": "PUT",
    "url": "http://localhost:8008/_matrix/client/v3/rooms/!AOaLmLFXUOIwuCDMJd%3Alocalhost/send/m.room.message/m1770541329288.4",
    "payload": {
      "msgtype": "m.text",
      "body": "delete pplease ",
      "m.mentions": {}
    },
    "response": {
      "status": 200,
      "statusText": "OK",
      "body": {
        "event_id": "$jze-n6g469reZzarAuLF-kQPfgNSMynuDX9otPLe6KI"
      }
    }
  }
"""

def generate_timestamp_random_string(length=16):
    timestamp_str = str(time.time_ns())
    characters = string.ascii_letters + string.digits
    random_len = max(0, length - len(timestamp_str))
    random_part = ''.join(random.choices(characters, k=random_len))
    combined_list = list(timestamp_str + random_part)
    random.shuffle(combined_list)
    final_string = ''.join(combined_list)[:length]
    
    return final_string


import requests

room_id = "!AOaLmLFXUOIwuCDMJd%3Alocalhost"
access_token = acquire_token()

headers = {
    "Authorization": f"Bearer {access_token}"
}

for i in range(1, 1001):
    url = f"http://localhost:8008/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{generate_timestamp_random_string()}"
    
    payload = {
        "msgtype": "m.text",
        "body": "boody mssg" + str(i),
        "m.mentions": {}
    }

    r = requests.put(url, json=payload, headers=headers)
    print(r.status_code, r.json())
