# Jupyter widget: Brillouin zone visualizer

[![PyPI - Version](https://img.shields.io/pypi/v/widget-bzvisualizer?color=4CC61E)](https://pypi.org/project/widget-bzvisualizer/)

A Jupyter widget to plot the 1st Brillouin zone of crystals. It is based on the corresponding Javascript library: https://github.com/materialscloud-org/brillouinzone-visualizer

The primary input is a crystal structure, which is parsed by [seekpath](https://github.com/giovannipizzi/seekpath) and the result is displayed by the Javascript widget using [anywidget](https://anywidget.dev/).

This repo is bootstrapped with `npm create anywidget@latest`.

## Installation & usage

```sh
pip install widget-bzvisualizer
```

For usage examples, see `example/example.ipynb`.

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

### Releasing and publishing a new version

In order to make a new release of the library and publish to PYPI, run

```bash
bumpver update --major/--minor/--patch
```

This will

- update version numbers, make a corresponding `git commit` and a `git tag`;
- push this commit and tag to Github, which triggers the Github Action that makes a new Github Release and publishes the package to PYPI.

## Acknowledgements

We acknowledge support from the EPFL Open Science Fund via the [OSSCAR project](http://www.osscar.org/).
