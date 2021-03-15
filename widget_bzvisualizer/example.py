import ipywidgets as widgets
from traitlets import Unicode, Dict, List
import seekpath
import numpy as np
import json

# See js/lib/example.js for the frontend counterpart to this file.

@widgets.register
class BZVisualizer(widgets.DOMWidget):
    """An example widget."""

    # Name of the widget view class in front-end
    _view_name = Unicode('BrillouinZoneView').tag(sync=True)

    # Name of the widget model class in front-end
    _model_name = Unicode('BrillouinZoneModel').tag(sync=True)

    # Name of the front-end module containing widget view
    _view_module = Unicode('widget-bzvisualizer').tag(sync=True)

    # Name of the front-end module containing widget model
    _model_module = Unicode('widget-bzvisualizer').tag(sync=True)

    # Version of the front-end module containing widget view
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    # Version of the front-end module containing widget model
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    # Widget specific property.
    # Widget properties are defined as traitlets. Any property tagged with `sync=True`
    # is automatically synced to the frontend *any* time it changes in Python.
    # It is synced back to Python from the frontend *any* time the model is touched.
    value = Unicode('Hello World!').tag(sync=True)

    # The cell parameters
    cell = List().tag(sync=True)

    # The jsondata for the Brillouin zone
    jsondata = Dict().tag(sync=True)

    def __init__(self, cell):
        super().__init__(cell = cell)

        structure = (np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), [[0., 0., 0.]], [1])
        test = seekpath.get_explicit_k_path(structure, reference_distance=0.025)
        
        with open("dou.json", "r") as f:
            self.jsondata = json.load(f)

