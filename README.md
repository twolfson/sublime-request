# sublime-request

Make HTTP requests from [Sublime Text 2][subl].

Attach to the `request` command via your keyboard shortcuts or add a custom command pallete to hook into.

[subl]: http://www.sublimetext.com/2

## Getting started

By default, no keyboards shortcuts or commands are added to the command pallete.

You are left to add in your own custom features since typing out HTTP parameters every time is tedious.

To add your own custom keyboard shortcut:

1. Open the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac
2. Navigate to "Preferences: Key Bindings - User"
3. Inside of the top level `[]`, add the following code

```json
{ "keys": ["alt+x"], "command": "request", "args": {"open_args": ["http://localhost:3000/"]} }
```

## Documentation
__TODO__

TODO: Allow for `open_args`, `open_kwargs`, `read_args`, `read_kwargs`.

## Examples
__TODO__

## License
Copyright (c) 2013 Todd Wolfson

Licensed under the MIT license.
