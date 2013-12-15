#!/usr/bin/env python
from django.core.management import execute_manager
import imp
import os

path = [os.path.join(os.path.abspath(os.path.dirname(__file__)),'saic')]
try:
    # Assumed to be in the same directory.
    imp.find_module('settings',path)
except ImportError:
    import sys
    sys.stderr.write("""Error: Can't find the file 'settings.py' in the directory %r. It appears you've customized things.\
      You'll have to run django-admin.py, passing it your settings module.\n""" % path)
    sys.exit(1)

import saic.settings

if __name__ == "__main__":
    execute_manager(saic.settings)
