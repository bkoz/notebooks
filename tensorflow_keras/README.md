# Tensorflow/Keras examples

Demos in this repo.

`01-cifar-10.ipynb` - Transfer learning ResNet architecture using the cifar10 data set. This notebook requires a GPU or it will take several hours vs. minutes to run. The notebook should take about 9 minutes to run on an nvidia T4 GPU. 

#### OpenDataHub configuration

- JupyterHub Notebook Image: `s2i-tensorflow-notebook-gpu:3.6`
- Container size: `Large`
- Number of required GPUs: `1`

##### JupyterHub notebook storage

Storage for JupyterHub defaults to 2Gi which may not suffice for some notebooks although the `01-cifar-10.ipynb` demo should work. Follow the procedure below to change the default notebook storage size.

OpenShift cluster admin privileges are needed.

- From the Jupyter UI, select the *control panel* and then *stop my server*.
- Using the `oc` client. 
  - Scale down the `jupyterhub` deployment config to 0 replicas. 
  - Edit the `jupyterhub-cfg` config map and increase the pvc size. 
  - Delete the `jupyterhub-nb-user-pvc` pvc.
  - Scale up `jupyterhub` deployment config. It should create a new pvc. 

[Tensor Flow Examples](https://github.com/tensorflow/docs.git)

=> docs/site/en/tutorials/keras/classification.ipynb

=> docs/site/en/tutorials/quickstart/beginner.ipynb

=> docs/site/en/tutorials/quickstart/advanced.ipynb

[Jason Dudash's Tensorflow demos](https://github.com/dudash/jupyter-gpu-examples)