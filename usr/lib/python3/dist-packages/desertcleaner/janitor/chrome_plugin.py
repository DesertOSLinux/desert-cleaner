from desertcleaner.janitor import JanitorCachePlugin


class ChromeCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш Chrome')
    __category__ = 'application'

    root_path = '~/.cache/google-chrome/Default'


class ChromiumCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш Chromium')
    __category__ = 'application'

    root_path = '~/.cache/chromium/Default'


class ChromiumSnapCachePlugin(JanitorCachePlugin):
    __title__ = _('Кеш Chromium')
    __category__ = 'application'

    root_path = '~/snap/chromium/common/.cache/chromium/Default'
