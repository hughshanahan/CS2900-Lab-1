# Lab 1

## Running in NoMachine

You can run Jupyter directly from the department server:

- First `git clone git@github.com:hughshanahan/CS2900-Lab-1.git` the repository and `cd` into the repository folder.
- Type, run `jupyter notebook` to launch the notebook in the browser.

You may have to copy and paste a URL from the output on the command line to the browser. 

![Example output to be copied from running jupyter notebook](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/CommandLineOutput.png)

![Paste to browser bar](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/PasteToBrowser.png)

Once it has loaded, you be greeted with this screen:

![Image of Binder dashboard](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/JupyterLaunchPage.png)

Double-click on the file "Lab1.ipynb". This should create a new tab with the following:

![Image of Jupyter notebook](https://github.com/hughshanahan/CS2900-Lab-1/blob/master/config/loaded_notebook.png)

Follow the instructions from there...

## Running on your own machine

Finally, you can also run Jupyter from your own computer. Instructions on
this can be found at
<a href="https://jupyter.org/install" class="uri">https://jupyter.org/install</a>. If you do not have it you, 
<a href="https://docs.anaconda.com/anaconda/install/" class="uri"> Anaconda </a> is a handy tool to download Python and Jupyter in one bundle.

You will need to clone the repository as above, and then launch your conda environment and install the packages in the `requirements.txt` folder. The main ones you will need are `numpy`, `matplotlib`, and `scipy`.

Make sure these are installed before starting the notebook!
