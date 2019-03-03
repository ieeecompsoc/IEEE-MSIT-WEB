#!/usr/bin/env python
import os

# database_config = {
#     'NAME' : 'ieeemsit_ieeemsit',
#     'USER' : 'ieeemsit',
#     'PASSWORD': 'psqlpassword'
# }

database_config = {
    'NAME' : 'ieee',
    'USER' : 'postgres',
    'PASSWORD': 'Siddharth@123'
}



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_root_path = os.path.join(BASE_DIR, 'static-root')

media_root_path = os.path.join(BASE_DIR, 'uploads')

Debug = True
