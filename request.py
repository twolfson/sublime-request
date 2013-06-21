# Load in dependencies
import sublime
import sublime_plugin
import urllib2


class RequestCommand(sublime_plugin.WindowCommand):
    def run(self, open_args=[], open_kwargs={}, read_args=[], read_kwargs={}, **kwargs):
        req = urllib2.urlopen(*open_args, **open_kwargs)
        req.read(*read_args, **read_kwargs)
