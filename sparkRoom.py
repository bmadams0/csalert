#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

#variables
url = 'https://api.ciscospark.com/v1/rooms'
payload = {'title': 'TEST ROOM'}
headers = {'content-type': 'application/json', 'authorization':'Bearer NTJiMTQyZjUtZTZlZC00N2I1LThjNTgtYWNmMjgyMDJhZmMyYzExYzY3YjQtNTdl'}

#API POST to create Spark Room
r = requests.post(url, data=json.dumps(payload), headers=headers)
