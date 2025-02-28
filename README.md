# 🚀 dontpanic

A very simple Python module to suppress `KeyboardInterrupt` traceback spam when pressing `^C`.

## Why?
By default, Python screams at you when you press `^C` to interrupt a script. (Proper languages like [Perl](https://www.perl.org/) don't do this.)

This module catches `KeyboardInterrupt` signals and handles them gracefully.

### Installation

```
pip install dontpanic
```

### Usage

```python
import dontpanic

print('Press control-C to interrupt this program')
while True:
    pass  # Press ^C to interrupt
```

... or with a custom message:

```python
import dontpanic

dontpanic.set_message("Exiting...")

print('Press control-C to interrupt this program')
while True:
    pass  # Press ^C to interrupt
```

![Don't Panic](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Don%27t_Panic.svg/512px-Don%27t_Panic.svg.png)
