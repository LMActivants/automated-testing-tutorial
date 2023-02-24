import os, sys
from configparser import ConfigParser
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from helpers.helper_web import get_browser

def before_all(context):
    config = ConfigParser()
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'behave.ini')
    config.read(initfile)

    # Reading the browser type from the configuration file
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func


def after_all(context):
    context.helperfunc.close()