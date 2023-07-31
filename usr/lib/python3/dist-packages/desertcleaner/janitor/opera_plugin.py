from desertcleaner.janitor import JanitorCachePlugin


class OperaCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш Opera')
    __category__ = 'application'

    root_path = '~/.opera/cache'
