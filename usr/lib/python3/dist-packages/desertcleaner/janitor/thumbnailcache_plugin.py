from desertcleaner.utils import system
from desertcleaner.janitor import JanitorCachePlugin


class ThumbnailCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш файлов')
    __category__ = 'personal'

    if system.CODENAME in ['precise']:
        root_path = '~/.thumbnails'
    else:
        root_path = '~/.cache/thumbnails'
