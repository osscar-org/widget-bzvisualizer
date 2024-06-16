# `widget-bzvisualizer`: A Jupyter Widget as Brillouin Zone Visualizer

[![PyPI - Version](https://img.shields.io/pypi/v/widget-bzvisualizer?color=4CC61E)](https://pypi.org/project/widget-bzvisualizer/)
[![widget test](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/widget-test.yml/badge.svg)](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/widget-test.yml)
[![screenshot comparison](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/screenshot-comparison.yml/badge.svg)](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/screenshot-comparison.yml)

A Jupyter widget to plot the 1st Brillouin zone of crystals. It is based on the corresponding Javascript library: https://github.com/materialscloud-org/brillouinzone-visualizer

The primary input is a crystal structure, which is parsed by [seekpath](https://github.com/giovannipizzi/seekpath) and the result is displayed by the Javascript widget using [anywidget](https://anywidget.dev/).

This repo is bootstrapped with `npm create anywidget@latest`.

<img src="./example/demo.gif" width='1200'>

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

### Github workflow testing

[![widget test](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/widget-test.yml/badge.svg)](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/widget-test.yml)

If the `widget test` fails, it indicates there is something wrong with the code, and the widget is NOT
being displayed correctly in the test.

[![screenshot comparison](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/screenshot-comparison.yml/badge.svg)](https://github.com/osscar-org/widget-bzvisualizer/actions/workflows/screenshot-comparison.yml)

If the `widget test` passes but the `screenshot comparison` fails, it indicates the appearance of the widget 
is different from the previous version. In this case, you'll need to manually download the artifact from 
the `widget test` and use it to replace the `widget-sample.png` figure in the `test` folder.

## Acknowledgements

We acknowledge support from the EPFL Open Science Fund via the [OSSCAR project](http://www.osscar.org/).

<img src='https://www.osscar.org/_images/logos.png' width='1200'>

