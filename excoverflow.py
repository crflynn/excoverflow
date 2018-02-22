"""Add stackoverflow and google search url to your uncaught exceptions."""
from functools import wraps
import sys

if sys.version_info[0] == 2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode


__version__ = '0.1.0'


sites = {
    "stackoverflow": {
        "url": "https://stackoverflow.com/search",
        "params": {"q": "[python] \"{name} {msg}\""}
    },
    "google": {
        "url": "https://www.google.com/search",
        "params": {"q": "python {name} {msg}"}
    }
}


def message(type, value, traceback):
    """Get the message to print after the traceback."""
    msg = ''
    for site in sorted(sites.keys()):
        params = sites[site]["params"]
        for param in params:
            params[param] = params[param].format(
                name=type.__name__,
                msg=value
            )
        msg += '\n' + sites[site]["url"] + "?" + urlencode(params)
    return msg


def wrapper(func):
    """Wrap the system excepthook with additional message."""
    @wraps(func)
    def wrapped_func(type, value, traceback):
        func(type, value, traceback)
        print(message(type, value, traceback))
        return
    return wrapped_func


# Wrap the uncaught exception handler
sys.excepthook = wrapper(sys.excepthook)
