#!/usr/bin/env python

import sys
import os
import logging
from gi.repository import Gtk

data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),'data')

# add our local site-packages which would normally be installed to system
sys.path.insert(1, os.path.join(os.path.dirname(__file__),'src/site-packages'))

# append local named icons to theme search path for named icons
theme = Gtk.IconTheme.get_default()
theme.append_search_path(os.path.join(data_dir, 'icons'))

from jsonhacker.application import Application

def install_excepthook():
    """ Make sure we exit when an unhandled exception occurs. """
    old_hook = sys.excepthook
    def new_hook(etype, evalue, etb):
        old_hook(etype, evalue, etb)
        while Gtk.main_level():
            Gtk.main_quit()
        sys.exit()
    sys.excepthook = new_hook
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG) # for run_local.py only!
    try:
        app = Application(package="json-hacker", 
                          package_name="JSON Hacker",
                          version="0-dev",
                          datadir=os.path.join(os.path.dirname(__file__), 'data'))
    except Exception, e:
        sys.exit("Could not initialize application: %s" % str(e))
    install_excepthook()
    r = app.run(sys.argv)
    sys.exit(r)  
