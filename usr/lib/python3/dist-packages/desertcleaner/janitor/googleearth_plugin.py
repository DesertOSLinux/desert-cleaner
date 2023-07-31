from desertcleaner.janitor import JanitorCachePlugin


class GoogleearthCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш Google Earth')
    __category__ = 'application'

    root_path = '~/.googleearth'
