# Jupyter widget: Brillouin zone visualizer

A Jupyter widget to plot the 1st Brillouin zone of crystals. It is based on the corresponding Javascript library: https://github.com/materialscloud-org/brillouinzone-visualizer

The primary input is a crystal structure, which is parsed by [seekpath](https://github.com/giovannipizzi/seekpath) and the result is displayed by the Javascript widget using [anywidget](https://anywidget.dev/).

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

## Acknowledgements

We acknowledge support from the EPFL Open Science Fund via the [OSSCAR project](http://www.osscar.org/).
