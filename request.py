# Load in core dependencies
import sublime
import sublime_plugin

# Attempt to load urllib.request/error and fallback to urllib2 (Python 2/3 compat)
try:
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportError:
    from urllib2 import urlopen, URLError


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
            req = urlopen(*open_args, **open_kwargs)
        except TypeError as err:
            # If the arguments are malformed, display the error
            return sublime.status_message(str(err))
        except URLError as err:
            # Otherwise, if there was a connection error, let it be known
            return sublime.status_message('Error connecting to "%s"' % url)

        # Let the user know we are making out request
        sublime.status_message('Requesting from "%s"' % url)

        # Read in the result and update the user
        result = req.read(*read_args, **read_kwargs)
        sublime.status_message('Successfully read from "%s"' % url)

        # If we should save result to clipboard, save it
        if save_to_clipboard:
            # DEV: For Sublime Text 3 support, we must coerce result from bytes into a string
            sublime.set_clipboard(str(result))
            sublime.status_message('Saved result from "%s" to clipboard' % url)
