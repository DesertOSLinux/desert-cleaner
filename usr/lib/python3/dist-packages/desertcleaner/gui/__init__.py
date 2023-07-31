import os
import logging

from gi.repository import Gtk

from desertcleaner.settings.constants import DATA_DIR


class GuiBuilder(object):
    def __init__(self, file_name):
        log = logging.getLogger('gui.GuiBuilder')

        file_path = os.path.join(DATA_DIR, 'ui', file_name)

        self.builder = Gtk.Builder()
        self.builder.set_translation_domain('desert-cleaner')
        self.builder.add_from_file(file_path)
        self.builder.connect_signals(self)

        for o in self.builder.get_objects():
            if issubclass(type(o), Gtk.Buildable):
                name = Gtk.Buildable.get_name(o)
                setattr(self, name, o)

    def get_object(self, name):
        return self.builder.get_object(name)
