from desertcleaner.janitor import JanitorCachePlugin


class EmpathyCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш Empathy')
    __category__ = 'application'

    root_path = '~/.cache/telepathy'
