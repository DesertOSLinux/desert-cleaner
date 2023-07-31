import gettext
import os

from gi.repository import GLib
from desertcleaner import __version__

__all__ = (
        'APP',
        'PACKAGE',
        'VERSION',
        'DATA_DIR',
        'init_locale',
        )


def applize(package):
    return ' '.join([a.capitalize() for a in package.split('-')])

PACKAGE = 'desert-cleaner'
VERSION = __version__
PKG_VERSION = VERSION
DATA_DIR = '/usr/share/desert-cleaner/'
APP = applize(PACKAGE)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_ROOT = os.path.join(GLib.get_user_config_dir(), 'desert-cleaner')
IS_INSTALLED = True

if not os.path.exists(CONFIG_ROOT):
    os.makedirs(CONFIG_ROOT)

try:
    LANG = os.getenv('LANG').split('.')[0].lower().replace('_', '-')
except:
    LANG = 'en-us'

if not __file__.startswith('/usr'):
    datadir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    DATA_DIR = os.path.join(datadir, 'data')
    IS_INSTALLED = False


def init_locale():
    global INIT
    try:
        INIT
    except:
        gettext.install(PACKAGE)

        INIT = True

init_locale()
