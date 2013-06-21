# Load in dependencies
import sublime
import sublime_plugin
import urllib2


# Setup request command for use
class RequestCommand(sublime_plugin.WindowCommand):
    def run(self, open_args=[], open_kwargs={},
            read_args=[], read_kwargs={}, save_to_clipboard=False,
            *args, **kwargs):
        # Make the request as requested
        # TODO: Update status bar with success/rejection
        req = urllib2.urlopen(*open_args, **open_kwargs)
        result = req.read(*read_args, **read_kwargs)

        # If we should save result to clipboard, save it
        if save_to_clipboard:
            # TODO: Update copy success
            sublime.set_clipboard(result)
