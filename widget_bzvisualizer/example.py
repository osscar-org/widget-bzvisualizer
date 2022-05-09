import ipywidgets as widgets
from traitlets import Unicode, Dict, List, Bool, Int, observe
import seekpath
from seekpath.brillouinzone.brillouinzone import get_BZ
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

    # The cell parameters, position and atomic numbers
    cell = List().tag(sync=True)
    positions = List().tag(sync=True)
    numbers = List().tag(sync=True)
    kpts = List().tag(sync=True)

    # The jsondata for the Brillouin zone
    jsondata = Dict().tag(sync=True)

    # Show the BZ surface
    face_color = Bool(True).tag(sync=True)

    # The path vectors
    path_vectors = List().tag(sync=True)

    # Singal to update the structure
    update_structure = Int().tag(sync=True)

    # Set the height of the widget
    height = Unicode('450px').tag(sync=True)

    # Set the width of the widget
    width = Unicode('100%').tag(sync=True)

    def __init__(self, cell, positions, numbers, face_color=True, height='450px', width='100%'):
        if type(cell) == np.ndarray:
            cell = cell.tolist()
        
        if type(positions) == np.ndarray:
            positions = positions.tolist()

        if type(numbers) == np.ndarray:
            numbers = numbers.tolist()

        super().__init__(cell = cell, positions=positions, numbers=numbers, face_color=face_color, height=height, width=width)

        system = (np.array(cell), np.array(positions), np.array(numbers))
        res = seekpath.getpaths.get_path(system, with_time_reversal=False)

        real_lattice = res["primitive_lattice"]
        rec_lattice = np.array(seekpath.hpkot.tools.get_reciprocal_cell_rows(real_lattice))
        b1, b2, b3 = rec_lattice

        faces_data = get_BZ(b1=b1, b2=b2, b3=b3)

        response = {}
        response["faces_data"] = faces_data
        response["b1"] = b1.tolist()
        response["b2"] = b2.tolist()
        response["b3"] = b3.tolist()
        ## Convert to absolute
        response["kpoints"] = {
            k: (v[0] * b1 + v[1] * b2 + v[2] * b3).tolist()
            for k, v in res["point_coords"].items()
        }
        response["kpoints_rel"] = {
            k: [v[0], v[1], v[2]] for k, v in res["point_coords"].items()
        }
        response["path"] = res["path"]

        # It should use the same logic, so give the same cell as above
        res_explicit = seekpath.get_explicit_k_path(system, with_time_reversal=False)
        for k in res_explicit:
            if k == "segments" or k.startswith("explicit_"):
                if isinstance(res_explicit[k], np.ndarray):
                    response[k] = res_explicit[k].tolist()
                else:
                    response[k] = res_explicit[k]

        if (
            np.sum(
                np.abs(
                    np.array(res_explicit["reciprocal_primitive_lattice"])
                    - np.array(res["reciprocal_primitive_lattice"])
                )
            )
            > 1.0e-7
        ):
            raise AssertionError("Got different reciprocal cells...")

        self.jsondata = response
        self.kpts = self.jsondata['explicit_kpoints_abs']
        self.path_vectors = self.jsondata['path']
        self.update_structure = 0

    @observe('cell')
    def _cell_change(self, change):
        system = (np.array(change['new']), np.array(self.positions), np.array(self.numbers))
        res = seekpath.getpaths.get_path(system, with_time_reversal=False)

        real_lattice = res["primitive_lattice"]
        rec_lattice = np.array(seekpath.hpkot.tools.get_reciprocal_cell_rows(real_lattice))
        b1, b2, b3 = rec_lattice

        faces_data = get_BZ(b1=b1, b2=b2, b3=b3)

        response = {}
        response["faces_data"] = faces_data
        response["b1"] = b1.tolist()
        response["b2"] = b2.tolist()
        response["b3"] = b3.tolist()
        ## Convert to absolute
        response["kpoints"] = {
            k: (v[0] * b1 + v[1] * b2 + v[2] * b3).tolist()
            for k, v in res["point_coords"].items()
        }
        response["kpoints_rel"] = {
            k: [v[0], v[1], v[2]] for k, v in res["point_coords"].items()
        }
        response["path"] = res["path"]

        # It should use the same logic, so give the same cell as above
        res_explicit = seekpath.get_explicit_k_path(system, with_time_reversal=False)
        for k in res_explicit:
            if k == "segments" or k.startswith("explicit_"):
                if isinstance(res_explicit[k], np.ndarray):
                    response[k] = res_explicit[k].tolist()
                else:
                    response[k] = res_explicit[k]

        if (
            np.sum(
                np.abs(
                    np.array(res_explicit["reciprocal_primitive_lattice"])
                    - np.array(res["reciprocal_primitive_lattice"])
                )
            )
            > 1.0e-7
        ):
            raise AssertionError("Got different reciprocal cells...")

        self.jsondata = response
        self.update_structure += 1