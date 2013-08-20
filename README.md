# sublime-request [![Donate on Gittip](http://badgr.co/gittip/twolfson.png)](https://www.gittip.com/twolfson/)

Make HTTP requests from [Sublime Text][subl].

Attach to the `request` command via your keyboard shortcuts or add a custom command pallete to hook into.

[subl]: http://www.sublimetext.com/

## Getting started
### Installation
This package is available under `Request` inside of [Package Control][pkg-control], a [Sublime Text][subl] plugin that allows for easy management of other plugins.

[pkg-control]: http://wbond.net/sublime_packages/package_control

If you prefer the manual route, you can install the script via the following command in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/sublime-request', 'request'], 'working_dir': path})
```

Packages can be uninstalled via "Package Control: Remove Package" via the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac.

### Working with the plugin
By default, no keyboards shortcuts or commands are added to the command pallete.

You are left to add in your own custom features since typing out HTTP parameters every time is tedious.

To add your own custom keyboard shortcut:

1. Open the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac
2. Navigate to "Preferences: Key Bindings - User"
3. Inside of the top level `[]`, add the following code

```json
{
  "keys": ["alt+x"],
  "command": "request",
  "args": {
    "open_args": ["http://google.com/"],
    "save_to_clipboard": true
  }
}
```

You now have `alt+x` bound to download [http://google.com/][google] to your clipboard.

[google]: https://www.google.com/

## Documentation
`sublime-request` is written on top of [Python][python]'s [`urllib2`][urllib2] library. We accept the following parameters:

[python]: http://python.org/
[urllib2]: http://docs.python.org/2/library/urllib2.html

- `open_args` - List of arguments to pass to `urllib2.urlopen`
- `open_kwargs` - Dictionary of keyword arguments to pass to `urllib2.urlopen`
- `read_args` - List of arguments to pass to `urllib2.urlopen`
- `read_kwargs` - Dictionary of keyword arguments to pass to `urllib2.urlopen`
- `save_to_clipboard` - Copies result from `read` to clipboard

### I don't know Python
This is a fact of life. Rather than creating a meta language to be just as simple, I will show you some commmon examples to draw from.

**Using open**
```js
{"open_args": [url, data, timeout]}

// Make GET request to google.com
// url = http://google.com/
{"open_args": ["http://google.com/"]}

// Make POST request to google.com. Switches to POST when data is included
// url = http://google.com/, data = "some=data"
{"open_args": ["http://google.com", "some=data"]}
```

**Using read**
```js
{"open_args": [buffer_length]}

// Read all of response from request
// buffer_length = null (None in Python)
{"open_args": ["http://google.com/"]}

// Read first 100 bytes of response
// buffer_length = 100
{"open_args": ["http://google.com"], "read_args": [100]}
```

## Examples
### Ping a server
Ping a server via a key binding (requests `http://localhost:3000/` when `alt+x` is pressed.

```
{
  "keys": ["alt+x"],
  "command": "request",
  "args": {
    "open_args": ["http://localhost:3000/"]
  }
}
```

### Grab some Lorem Ipsum
Copy the first 100 characters of Lorem Ipsum to your clipboard via a key binding, `alt+x`.

```
{
  "keys": ["alt+x"],
  "command": "request",
  "args": {
    "open_args": ["http://loripsum.net/api/plaintext"],
    "read_args": [100],
    "save_to_clipboard": true
  }
}
```

## FAQ
### I want to see the results of my request.
[Sublime Text][subl] comes default with an `exec` command which runs CLI commands in a panel. There are no official docs to my knowledge but you can find the source code via `Command Pallete -> Browse Packages -> Default/exec.py@class ExecCommand`.

Here is a key binding that runs `curl` to [http://google.com/][google].

```json
{
  "keys": ["alt+x"],
  "command": "exec",
  "args": {
    "cmd": ["curl", "http://google.com/"]
  }
}
```

```sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   219  100   219    0     0   2565      0 --:--:-- --:--:-- --:--:--  5918
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
[Finished in 0.1s]
```

## License
Copyright (c) 2013 Todd Wolfson

Licensed under the MIT license.
