# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:04:00 2019

@author: Petros.Kalendralis
"""

import xnat
with xnat.connect('https://xnat.bmia.nl/', user='username') as connection: 
    connection.services.import_('local_path', content_type='application/zip', project='projectname', subject='subjectname', experiment='experimentname')