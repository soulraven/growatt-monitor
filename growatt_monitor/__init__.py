#  -*- coding: utf-8 -*-
# A Python "namespace package" http://www.python.org/dev/peps/pep-0382/
# This always goes inside a namespace package's __init__.py

from pkgutil import extend_path

from .version import __version__

__path__ = extend_path(__path__, __name__)
