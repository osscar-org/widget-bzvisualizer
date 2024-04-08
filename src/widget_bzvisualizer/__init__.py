import importlib.metadata
import pathlib

import anywidget
import traitlets

from . import utils

try:
    __version__ = importlib.metadata.version("widget_bzvisualizer")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class BZVisualizer(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"

    seekpath_data = traitlets.Dict({}).tag(sync=True)

    # parameters passed to the js BZVisualizer
    show_axes = traitlets.Bool(True).tag(sync=True)
    show_bvectors = traitlets.Bool(True).tag(sync=True)
    show_pathpoints = traitlets.Bool(False).tag(sync=True)
    disable_interact_overlay = traitlets.Bool(False).tag(sync=True)

    # Parameters to control the size of the div-container
    width = traitlets.Unicode("100%").tag(sync=True)
    height = traitlets.Unicode("400px").tag(sync=True)

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
        self.seekpath_data = utils.get_seekpath_data_for_visualizer(
            cell, rel_coords, atom_numbers
        )
