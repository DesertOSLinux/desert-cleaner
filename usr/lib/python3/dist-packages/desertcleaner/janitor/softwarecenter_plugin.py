from desertcleaner.janitor import JanitorCachePlugin


class SoftwareCenterCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш магазина приложений')
    __category__ = 'application'

    root_path = '~/.cache/software-center'
