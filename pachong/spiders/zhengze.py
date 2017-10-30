# -*- coding: utf-8 -*-
import re


pattern = re.compile(r'http[^s]://www.python.org]')
result = re.match(pattern,'http://www.python.org')
print(result)