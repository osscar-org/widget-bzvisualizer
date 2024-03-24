# Jupyter widget: Brillouin Zone visualizer

Jupyter widget based on the corresponding Javascript library: https://github.com/materialscloud-org/brillouinzone-visualizer

The primary input is a crystal structure. The code runs [seekpath](https://github.com/giovannipizzi/seekpath) and displays the Javascript widget using [anywidget](https://anywidget.dev/).

This repo is bootstrapped with `npm create anywidget@latest`.

## Installation

```sh
pip install widget_bzvisualizer
```

## Development

Install the python code:

```sh
pip install -e .[dev]
```

You then need to install the JavaScript dependencies and run the development server.

```sh
npm install
npm run dev
```

Open `example/example.ipynb` in JupyterLab, VS Code, or your favorite editor to start developing. Changes made in `js/` will be reflected in the notebook.
