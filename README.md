# sublime-request

Make HTTP requests from [Sublime Text 2][subl].

Attach to the `request` command via your keyboard shortcuts or add a custom command pallete to hook into.

[subl]: http://www.sublimetext.com/2

## Getting started
### Installation
Currently, this package is not available via [Package Control][pkg-control]. In the meantime, you can install the script via the following command in the Sublime Text 2 terminal (`ctrl+\``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/sublime-request', 'request'], 'working_dir': path})
```

Packages can be uninstalled via "Package Control: Remove Package" via the comand pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac.

### Working with the plugin
By default, no keyboards shortcuts or commands are added to the command pallete.

You are left to add in your own custom features since typing out HTTP parameters every time is tedious.

To add your own custom keyboard shortcut:

1. Open the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac
2. Navigate to "Preferences: Key Bindings - User"
3. Inside of the top level `[]`, add the following code

```json
{ "keys": ["alt+x"], "command": "request", "args": {"open_args": ["http://google.com/"], "save_to_clipboard": true} }
```

You now have `alt+x` bound to download [http://google.com/][google] to your clipboard.

[google]: https://www.google.com/

## Documentation
__TODO__

TODO: Allow for `open_args`, `open_kwargs`, `read_args`, `read_kwargs`, `save_to_clipboard`

## Examples
__TODO__

## License
Copyright (c) 2013 Todd Wolfson

Licensed under the MIT license.
