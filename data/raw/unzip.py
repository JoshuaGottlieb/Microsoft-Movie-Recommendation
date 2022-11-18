#!/usr/bin/env python3

import os
import zipfile
import gzip
import shutil

zipped_path = '../zipped/'

for file in os.listdir(zipped_path):
    if file.endswith('zip'):
        with zipfile.ZipFile(zipped_path + '/' +  file, 'r') as f:
            f.extractall('./')
    elif file.endswith('.gz'):
        with gzip.open(zipped_path + '/' + file, 'rb') as f_in:
            with open('./' + file[:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


