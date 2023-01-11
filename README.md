# CS2900 Lab 1

## Running on Binder
Please click on the launch Binder icon below. 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hughshanahan/CS2900-Lab-1/HEAD)


It will take a few minutes to launch....

When it launches you should see the following:

![Image of Binder loading](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/binder_loading.png)

Once it has loaded, you be greeted with this screen:

![Image of Binder dashboard](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/binder_dashboard.png)

Double-click on the file "Lab1.ipynb". This should create a new tab with the following:

![Image of Jupyter notebook](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/loaded_notebook.png)

Follow the instructions from there...

# If Binder doesn't work you can run the notebooks locally

## Running in NoMachine

You can run Jupyter directly from the department server:

- First `git clone` the repository and `cd` into the repository folder.
- Run `pip3 install okpy`
- Type, run `jupyter notebook` to launch the notebook in the browser.

## Running on your own machine

Finally, you can also run Jupyter from your own computer. Instructions on
this can be found at
<a href="https://jupyter.org/install" class="uri">https://jupyter.org/install</a>. If you do not have it you, 
<a href="https://docs.anaconda.com/anaconda/install/" class="uri"> Anaconda </a> is a handy tool to download Python and Jupyter in one bundle.

You will need to clone the repository as above, and then launch your conda environment and install the packages in the `requirements.txt` folder. The main ones you will need are `okpy`, `numpy`, `matplotlib`, and `scipy`.

Make sure these are installed before starting the notebook!
