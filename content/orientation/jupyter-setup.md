# JupyterLab + SoS Suite setup

## Operating OS requirement

The instructions on this page are tested and known to work for Linux and MacOS. It has not been tested on Windows. Although with some efforts it might work for Windows, using Windows your every day computational biology research is discouraged.
If you don't have access to other types of OS, an alternative is to set up a Linux OS under your Windows OS using [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Install miniconda3 the Python development environment

We recommend using `miniconda` over `anaconda` and customize your installation as needed after install this minimal version of `conda`. 
To install please follow instructions [on this page](https://docs.conda.io/en/latest/miniconda.html). Please go for `miniconda3`.

You can download the installer via command tool if you are on a Linux server without graphical interface. For example:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Or, download it and upload to the server using command tools such as `scp`. Then run:


```
bash Miniconda3-latest-Linux-x86_64.sh
```

to install. After following the prompts in the installation process you should find in `~/.bashrc` or `~/.bash_profile` a line like this:

```bash
export PATH=$HOME/miniconda3/bin:$PATH
```

and type `source ~/.bashrc` (or `source ~/.bash_profile`) to load the changes. To verify you've installed it successfully:

```
which python
```
It should show the path as `$HOME/miniconda3/bin/python`. 

After you successfully installed the latest version of `miniconda3`, please follow prompts below to setup
a [JupyterLab + SoS Suite environment](https://doi.org/10.1371/journal.pcbi.1006843) for daily computing.

**Note:** maybe you already have a version of `anaconda` or `miniconda` on your computer. If you are very familiar with `conda` then please try to work with your existing version by either upgrading or create separate `env` under it to install additional packages. You might also want to start afresh and retire your older version (but keep the installation around for a while just in case). A simple approach is to rename your `miniconda3` folder to, say `miniconda3_bak`, and install the new `miniconda3`.

**Note** It is of crucial importance that after the installation of conda, `conda init` command shall not be ran for reason outlined in issue [#3](https://github.com/gaow/lab-wiki/issues/3).


## `conda` vs `pip` for package installation

With `miniconda` there are two ways to install Python packages: either using `conda install` or `pip install`. We will provide instructions for both methods below but you only have to choose one approach: **either `conda` or `pip` but not both**.

I wouldn't discuss too much details on what each does and pros and cons. I'd just say that:

1. it is recommended to consistently use either `conda` or `pip` and **not** a combination of them
2. for those savvy in Python and in package management in general, I recommend using `pip` over `conda`. For novices perhaps `conda` is easier. 
3. Do not use `conda` to install R and R packages: from my experience, this is not recommended --- it creates more issues than convenience at least to me. On a cluster you can try to load the R software that the cluster system has already installed, then install packages to your home directory. You should be asked to set or confirm the path to install R packages to in your `HOME` directory.
4. Do not use `conda activate` or `conda init` on the cluster, the codes introduced by it in .bashrc has proven to cause a wide array of problem including segmentation fault or compilation errors.

**Note: if the installation commands below generates timeout errors on your cluster system**,

- On Columbia CUMC cluster, you need to add these commands below to your .bashrc and then source it to set network proxy:

```
export http_proxy=http://bcp3.cumc.columbia.edu:8080
export https_proxy=http://bcp3.cumc.columbia.edu:8080
```
- If you are in China you might need to [try a different mirror](https://www.jb51.net/article/163315.htm), depending on your location. For example use a mirror at Tsinghua University, `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ...`, may help. You can also [configure `bash` or `pypi` to use alternative mirrors by default](https://wiki.onap.org/display/DW/Configure+and+customize+pip).

## `pip` installation for SoS, JupyterLab and kernels

### Base notebook

```
pip install notebook jupyterlab jupyter_contrib_nbextensions
```

### SoS Suite

```
pip install docker markdown wand graphviz imageio pillow nbformat feather-format --no-cache-dir
pip install sos sos-notebook sos-r sos-pbs sos-python sos-bash -U --no-cache-dir
python -m sos_notebook.install
pip install jupyterlab-sos -U --no-cache-dir
```

### Bash kernel

```
pip install bash_kernel --no-cache-dir
python -m bash_kernel.install
```

### Markdown kernel

```
pip install markdown-kernel --no-cache-dir
python -m markdown_kernel.install 
```

### R kernel

You need to install R first. Here are [some tips for Debian based Linux](../productivity_tips/debian-setup) (possibly outdated).
For MacOS you can download the [R software installer from CRAN](https://cran.r-project.org/bin/macosx/) and install from there.

I recommand against installing R via `conda` unless you are familiar with the setup -- in short, (as of 2019) the default configuration can cause various issues for other packages.

To install R kernel for Jupyter after you installed R,

```
R --slave -e "IRkernel::installspec()"
```

If you get a complaint that `IRkernel` package is not available, please install it in R, eg `install.packages('IRkernel')`, before you run the command above.


**Note** On our cluster, R is pre-installed and specific version of R needs to be loaded, e.g. `module load R/4.0` . After module loaded, enter the R interface and install the package needed. If the R complaint about C++ enviorment, try removed the code chunk in .bashrc that are under by `conda initiation` session 


### nbdime to work with git

This will override the default `git diff` and display better the changes to IPython notebooks
```
pip install nbdime
nbdime config-git --enable --global
```

## `conda` installation for SoS, JupyterLab and kernels

**You can ignore this section if you already installed everything using `pip` as shown above**

You can install JupyterLab with SoS using commands below. It will automatically install the `transient-display-data` extension, `jupyterlab`, `sos-notebook`, and `sos` if needed.

```
conda install jupyterlab-sos -c conda-forge
```

You will need to install nodejs>=12.0.0 to upgrade JupyterLab extensions. To install a specific version just type:

```
conda install nodejs==15.12.0 -c conda-forge
```

To install the kernels, type:

```
conda install sos-r sos-python sos-pbs sos-bash markdown-kernel -c conda-forge
```

Finally upgrade your extensions to the latest version by typing:

```
jupyter labextension update --all
```
At this point everything you need should be installed. 
## What if Jupyter kernels keep dying?

This happened to us several times, and solution [on this ticket](https://github.com/jupyter/notebook/issues/1892) was the rescue.

## Install Docker

**Notice: docker cannot be installed on many HPC cluster environments due to security reasons. Please skip this step if you are on the cluster. We may use `singularity` instead of `docker` to run some applications on cluster. But still having docker configured on your laptop or desktop computer can be useful.**

We use Docker a lot running various software that are hard to install. SoS also provides an interface to run Docker images. 

To install Docker on Linux,

- Run commands below:

```
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

- Log out and log back in (no need to reboot computer)

To install it on MacOS, visit https://www.docker.com/products/docker-desktop and download & install the Docker Desktop installer.
