import logging

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from desertcleaner.gui import GuiBuilder
from desertcleaner.settings.constants import VERSION
from desertcleaner.janitor import JanitorPage
from desertcleaner.utils import icon

log = logging.getLogger('app')


class DesertCleanerWindow(GuiBuilder):
    feature_dict = {}

    def __init__(self):
        GuiBuilder.__init__(self, file_name='mainwindow.xml')
        self.load_janitor()
        self.mainwindow.show()

    def on_mainwindow_destroy(self, widget=None):
        Gtk.main_quit()
        exit()

    def on_about_button_clicked(self, widget):
        self.aboutdialog.set_version(VERSION)
        self.aboutdialog.set_transient_for(self.mainwindow)
        self.aboutdialog.run()
        self.aboutdialog.hide()

    def load_janitor(self):
        janitor_page = JanitorPage()
        self.feature_dict['janitor'] = self.notebook.append_page(janitor_page, Gtk.Label('janitor'))
        self.module_image.set_from_pixbuf(icon.get_from_name('computerjanitor', size=48))
        self.title_label.set_markup('<b><big>%s</big></b>' % _('Очистка компьютера'))
        self.description_label.set_text(_("Очистить систему от мусора и ненужных файлов"))
