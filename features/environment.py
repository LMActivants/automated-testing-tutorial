import os, sys
from configparser import ConfigParser
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from helpers.helper_web import get_browser

def before_all(context):
    config = ConfigParser()
    my_file = (os.path.join(os.getcwd(), 'behave.ini'))
    config.read(my_file)

    # Reading the browser type from the configuration file
    helper_func = get_browser('chrome')
    context.helperfunc = helper_func


def after_all(context):
    context.helperfunc.close()