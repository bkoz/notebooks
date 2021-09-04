# SciPy Examples

## How to 

[01-py-slicer](01-py-slicer.ipynb) - A NumPy tutorial that works with medical images. A GPU is not required.

### 1) Open Data Hub

Choose the `s2i-generic-data-science-notebook:v0.0.2` container image when launching Jupyter hub.

Once Jupyter lab appears, visit the `data-science-notebooks/01-py-slicer.ipynd` notebook file.

### 2) Run on Binder or Google Collab

[01-py-slicer](01-py-slicer.ipynb) - A NumPy tutorial that works with medical images.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/redhat-naps-da/data-science-notebooks/main?filepath=scipy%2F01-py-slicer.ipynb)
[![Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/bkoz/6af632c482e320f28adb815b28d8f608/01-py-slicer.ipynb)


### 3) A local Python 3.8 environment

```
$ python3 -m venv scipy-demos
$ source scipy-demos/bin/activate
$ pip install pip --upgrade
$ pip install -r requirements.txt
```

Configure and run the Jupyter notebook server.

```
$ jupyter nbextension enable --py widgetsnbextension
$ jupyter lab --ip=0.0.0.0
```

#### TODO

Incorporate [3D image classification](https://keras.io/examples/vision/3D_image_classification/) into this.



