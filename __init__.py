# By default, we configure logging to be non-silent. Use `restore_defaults()`
# from `pylearn2.utils.logger` to revert this behaviour.
import sys
sys.path.append("E:\\360MoveData\\Users\\zx305\\Documents\\GitHub\\pylearn2")
# sys.path.append("E:\\360MoveData\\Users\\zx305\\Documents\\GitHub")


# from pylearn2.utils.logger import configure_custom
from pylearn2.utils.logger import configure_custom

# TODO: make it configurable whether we pass debug=True here. By default
# debug=False.
configure_custom()

# Remove this from the top-level namespace.
del configure_custom


