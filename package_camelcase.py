"""
1. Installing package in python as follows

# macOS
sudo python3 -m pip install matplotlib

# Windows (may require elevation)
python -m pip install matplotlib

# Linux (Debian)
sudo apt-get install python3-tk
python3 -m pip install matplotlib

2. Just import and run


"""

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))



#search for package in https://pypi.org/

#uninstalling 
#pip uninstall camelcase

#list packages
#pip list