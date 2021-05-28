# -*- coding:utf8 -*-

import json

data = "D017:输电"
result = {}
x = data.split(":", 1)
result["name"] = x[1]
result['id'] = x[0]
print(result)

