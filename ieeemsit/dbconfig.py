#!/usr/bin/env python
import os

database_config = {
    'NAME' : 'ieeemsit_ieeemsit',
    'USER' : 'ieeemsit',
    'PASSWORD': 'psqlpassword'
# database_config = {
#     'NAME' : 'ieeemsit_ieeemsit',
#     'USER' : 'sahilkhurana',
#     'PASSWORD': 'psqlpassword'
# }

#database_config = {
    #'NAME' : 'ieeemsit2',
    #'USER' : 'ankush2',
    #'PASSWORD': 'garg123ankush'
#}



#database_config = {
#    'NAME' : 'ieeemsit2',
#    'USER' : 'ankush2',
#    'PASSWORD': 'garg123ankush'
#}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_root_path = os.path.join(BASE_DIR, 'static-root')

media_root_path = os.path.join(BASE_DIR, 'uploads')

Debug = False
