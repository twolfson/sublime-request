# Load in dependencies
import sublime
import sublime_plugin
import urllib2


# Setup request command for use
class RequestCommand(sublime_plugin.WindowCommand):
    def run(self, open_args=[], open_kwargs={},
            read_args=[], read_kwargs={},
            save_to_clipboard=False):
        # Make the request as requested
        url = open_args[0] or open_kwargs.get('url', None)

        # Attempt to open the url
        try:
            # Make our open request
            req = urllib2.urlopen(*open_args, **open_kwargs)
        except TypeError as err:
            # If the arguments are malformed, display the error
            return sublime.status_message(str(err))
        except urllib2.URLError as err:
            # Otherwise, if there was a connection error, let it be known
            return sublime.status_message('Error connecting to "%s"' % url)

        # Let the user know we are making out request
        sublime.status_message('Requesting from "%s"' % url)

        # Read in the result and update the user
        result = req.read(*read_args, **read_kwargs)
        sublime.status_message('Successfully read from "%s"' % url)

        # If we should save result to clipboard, save it
        if save_to_clipboard:
            sublime.set_clipboard(result)
            sublime.status_message('Saved result from "%s" to clipboard' % url)