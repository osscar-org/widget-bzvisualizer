import importlib.metadata
import pathlib

import anywidget
import traitlets as tl

from . import utils

try:
    __version__ = importlib.metadata.version("widget_bzvisualizer")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BZVisualizer(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    # primary input parameters, not directly used in the JS app
    cell = tl.List().tag(sync=True)
    rel_coords = tl.List().tag(sync=True)
    atom_numbers = tl.List().tag(sync=True)

    # auxiliary traitlet to easily manage the previous ones
    system = tl.Dict({}).tag(sync=True)

    # Data used in the JS app
    seekpath_data = tl.Dict({}).tag(sync=True)

    # optional parameters passed to the JS BZVisualizer
    show_axes = tl.Bool(True).tag(sync=True)
    show_bvectors = tl.Bool(True).tag(sync=True)
    show_pathpoints = tl.Bool(False).tag(sync=True)
    disable_interact_overlay = tl.Bool(False).tag(sync=True)

    # parameters to control the size of the div-container
    width = tl.Unicode("100%").tag(sync=True)
    height = tl.Unicode("400px").tag(sync=True)

    def __init__(
        self,
        cell,
        rel_coords,
        atom_numbers,
        **kwargs,
    ):
        """Method to create the widget.

        The traitlets defined above can be set as a kwargs.
        """
        super().__init__(**kwargs)
        self.system = {
            "cell": cell,
            "rel_coords": rel_coords,
            "atom_numbers": atom_numbers,
        }
        self.seekpath_data = utils.get_seekpath_data_for_visualizer(self.system)

    @tl.observe("cell")
    def _cell_changed(self, change):
        self.system[change["name"]] = change["new"]
        self.seekpath_data = utils.get_seekpath_data_for_visualizer(self.system)
