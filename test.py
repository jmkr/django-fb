import imp
try:
    import sys
    #print sys.path
    installed_modules = u'./lib/python2.6/site-packages'
    if installed_modules not in sys.path:
        sys.path.append(installed_modules)
    imp.find_module('bootstrapped') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'bootstrap' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)
