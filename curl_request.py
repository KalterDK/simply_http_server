#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"userId":"1", "username":"roman b3zz"}'

response = requests.post('http://192.168.19.14:9090/foo', headers=headers, data=data)