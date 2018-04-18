#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"userId":"1", "username":"User some_data"}'

response = requests.post('http://127.0.0.1:9090/foo', headers=headers, data=data)
