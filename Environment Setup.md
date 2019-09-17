# Integrating Pandas with Scikit-Learn, an Exciting New Workflow

## Environment Setup Instructions

This document contains instructions for setting up your environment for the [Integrating Pandas with Scikit-Learn, an Exciting New Workflow][3] tutorial presented by Ted Petrou during ODSC East in Boston on April, 30th at 9:00 A.M.

## GitHub Repository

Visit [this current GitHub repository][2] and click the 'Clone or Download' green button on the right to download all of the material.

## Software Requirements

This tutorial relies on you having the following installed:

* Python 3.6+
* pandas
* scikit-learn version 0.20
* Jupyter Notebook


## Create a conda environment

I recommend using the conda package manager to create a separate environment just for this tutorial. If you do not have the conda package manager, you can download it with the rest of the [Anaconda distribution here][1]. If you wish to only install conda, you may instead download [Miniconda][4]. For either installation choose Python 3.7 (or whatever latest version of Python is available).

Create a file titled 'environment.yml'. If you have already downloaded the material from GitHub, then this file will have already been created for you. Place the exact contents of the following in the file and save it.

```yml
name: pandas_scikit_learn
channels:
  - conda-forge
dependencies:
 - python=3.7
 - pandas
 - scikit-learn=0.20
 - jupyter
```

### Command to create new environment

On your command line, navigate to the directory where the 'environment.yml' file was created and run the following command.

```
conda env create -f environment.yml
```

The above command will take some time to complete. Once it completes, the environment `pandas_scikit_learn` will be created with pandas, scikit-learn, jupyter, and all of their dependencies.

### List the environments

Run the command `conda env list` to show all the environments you have. There will be a `*` next to the active environment, which will likely be `base`, the default environment that everyone starts in.

### Activate the pandas_scikit_learn environment

Creating the environment does not mean it is active. You must activate in order to use it. Use the following command to activate it.

```
conda activate pandas_scikit_learn
```

You should see `pandas_scikit_learn` in parentheses preceding your command prompt. You can run the command `conda env list` to confirm that the `*` has moved to `pandas_scikit_learn`.

### Run python code from the pandas_scikit_learn environment

Let's further confirm that we are in the `pandas_scikit_learn` environment by running some code within it. Start the IPython shell (ipython is a jupyter dependency and installed during environment creation) by running the following command:

```
ipython
```

Within the ipython shell, you can use the `sys` module to find the location of the python executable. Run the following commands now.

```
In [1]: import sys

In [2]: sys.executable
Out[2]: '/Users/Ted/anaconda3/envs/pandas_scikit_learn/bin/python'
```

The executable location should end with `anaconda3/envs/pandas_scikit_learn/bin/python`.

### Ensuring that Jupyter Notebooks run from this environment

We will now verify the location of the python executable within a Jupyter Notebook. You might be wondering why this is necessary since we did nearly the same thing in the previous step. Surprisingly, Jupyter Notebooks are able to run any python executable from any environment. Your environment might not be set up properly to run the python installation from the active environment.

Exit out of the IPython shell that you started above and ensure you are still in the `pandas_scikit_learn` environment. Launch a jupyter notebook with the following command:

```
jupyter notebook
```

After the home page finishes loading in your browser, create a new notebook by clicking the **New** button in the top right hand side of the page. Choose 'Python 3' in the dropdown menu. Within the notebook's first cell, run the same commands as before:

```
import sys
sys.executable
```

**One of two possibilities can happen**

If the value outputted from `sys.executable` is the same as it was from the ipython shell, then your environment is set up properly and you are good to go and may skip down to the [Deactivate environment](#Deactivate-environment) section.

If the value outputted from `sys.executable` ends with the following:

```
anaconda3/bin/python
```

then you have more work to do and the code you are executing is from the base environment and not from `pandas_scikit_learn`.

### Deleting the "User" Kernel

Exit out of Jupyter and return to the command line. We need to delete a [Kernel][5], a program that "runs and introspects the user’s code".

As mentioned earlier, Jupyter Notebooks allow you to run any python executable regardless of the environment that it was launched from. It uses kernels to run these different python executables. Jupyter has three different locations in your file system to find the kernel to run. These locations are known as **User**, **Env**, and **System**. Open up the [official documentation][6] to find the locations for your operating system.

One issue is that kernels can have the same name. In fact, every single environment that you install jupyter in will have its own Env 'Python 3' kernel. But, the User kernels have the highest priority and will be run if there is a name collision with the Env kernels. 

It's likely that you have a User 'Python 3' kernel that is interfering with your Env 'Python 3' kernel. Let's list the currently available kernels with the following command:

```
jupyter kernelspec list
```

You will see the name of the kernels followed by its location. You should see that the 'Python 3' kernel is located in the User location. On my Mac, it shows the following:

```
/Users/Ted/Library/Jupyter/kernels
```

This kernel takes precedence and will be run regardless of the environment you launch your notebook from. This is extremely confusing and frustrating in my opinion. It would make more sense if the only available kernels were from the active environment.

Running the above command will actually not list kernels with the same name that have lower priority. For instance, since you installed jupyter in the `pandas_scikit_learn` environment, it will have its own 'Python 3' kernel in the Env location. It is not going to be shown in the list above. Instead, you can list this kernel manually. We can find the location of the Env kernels again by [looking at the documentation][6]. On my Mac, the following command lists all my kernels in the `pandas_scikit_learn` environment.

```
ls /Users/Ted/anaconda3/envs/pandas_scikit_learn/share
```

This returns 'Python 3', a kernel with the same name returned from `jupyter kernelspec list` but in a different location. For personal machines, there is usually not a need to have a User 'Python3' kernel so we can delete it. The following command will delete the 'Python 3' kernel with the highest priority. Only run it if you have a User 'Python 3' kernel.

```
jupyter kernelspec remove python3
```

Rerunning `jupyter kernelspec list` should now return the Env 'Python 3' kernel. Check that it does so now.

### Verify from a Jupyter Notebook

We should still verify that the python executable location has changed within the notebook. Start by running `jupyter notebook` again and starting the same notebook that you ran the command `sys.executable` in. Run this command again and verify that the python executable is now located in the `pandas_scikit_learn` environment.

### No need to do this in future environments

You will not have to repeat this procedure when creating new environments that have jupyter installed in them. The User 'Python 3' kernel is permanently deleted and jupyter now uses the Env location as its default. Every new environment that you create with jupyter will have its own 'Python 3' kernel that will be the default.

### Alternative - Create a new kernel with a different name

Instead of deleting the User 'Python 3' kernel, you may create a new User(or Env) kernel with a distinct name. The following command creates a new User kernel named 'pandas_scikit_learn_python3' displayed as 'Python 3 (pandas_scikit_learn)'.

```
python -m ipykernel install --user --name pandas_scikit_learn_python3 --display-name "Python 3 (pandas_scikit_learn)"
```

Since the above is a User kernel, it will be available from any environment. To run a notebook with this kernel, select it from the dropdown menu from the 'New' button. You can instead install an Env kernel by changing the `--user` option to `--sys-prefix`.

### Deactivate environment

You should only use the `pandas_scikit_learn` environment for this tutorial. When you are done with this session, run the command `conda deactivate` to return to your default conda environment.

[1]: https://www.anaconda.com/distribution/
[2]: https://github.com/tdpetrou/integrating-pandas-with-scikit-learn
[3]: https://odsc.com/training/portfolio/integrating-pandas-with-scikit-learn-an-exciting-new-workflow
[4]: https://docs.conda.io/en/latest/miniconda.html
[5]: https://jupyter-client.readthedocs.io/en/latest/kernels.html#making-kernels-for-jupyter
[6]: https://jupyter-client.readthedocs.io/en/stable/kernels.html#kernel-specs
