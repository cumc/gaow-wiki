# A beginner's note on Linux Mint Desktop

This page documents some tips for beginner users on [Linux Mint Desktop environment](https://linuxmint.com/).

## Setup

You can download the [latest system ISO file](https://linuxmint.com/download.php) and build the system to a USB drive using, eg, [netbootin](https://unetbootin.github.io/). You then restart your computer, boot it from USB (might have to change your BIOS default boot sequence in order to start from a USB), follow prompts until you get into the "live" operating system. There you will find on the Desktop an icon to "Install Mint". Double click on it and follow the prompts to install the system. When in doubt, use default settings. After installing please quit the live system, unplug the USB drive and restart to login to the system.

Once you are logged in, please feel free to poke around changing small (yet important) details such as font size, terminal theme and fonts, display preferences etc. The default web browser is Firefox. If you prefer other browsers, you can download [Google Chrome](https://www.google.com/chrome/), double click on the installer and follow prompts to install Google Chrome. 

If you use Linux Mint 20.x, you can use [this script](https://github.com/gaow/misc/blob/master/bash/linux_setup.sos) to install some basic software packages. To do so, first install `miniconda` and `SoS`,

```
install_dir='$HOME/miniconda3'
curl -fsSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && bash /tmp/miniconda.sh -bfp $install_dir
echo "export PATH=$install_dir/bin:\$PATH" >> ~/.bashrc && source ~/.bashrc
chown -R $USER.users $install_dir && mkdir -p ~/.conda && chown -R $USER.users ~/.conda
pip install sos
```

Then download the script and install recommended software packages

```
wget https://raw.githubusercontent.com/gaow/misc/master/bash/linux_setup.sos
sudo chmod +x linux_setup.sos
./linux_setup.sos ubuntu_focal:1-5
```

If you need an Rstudio server on your machine please follow [these instructions](https://www.rstudio.com/products/rstudio/download-server/debian-ubuntu/) to install, and [this page](https://support.rstudio.com/hc/en-us/articles/200552306-Getting-Started) to set it up.

## Access software programs available

The icon for software manu is on the bottom left corner of the screen. Click on it, then type in the search box for programs you want to bring up, eg type `screen`, you will be given a list of programs for display management, power management and screenshot programs. Click on the program you would like to launch.

## Edit text files

The default text editor in Linux Mint is `xed`. If you would like to trigger it from the terminal, simply type `xed` as a command, eg, 

```
xed /path/to/file.txt
```

## Connect to this computer from another one

[This page](http://statgen.us/lab-wiki/productivity_tips/remote-computer) documents three ways to connect from another computer to this computer:

1. bash terminal
2. Juypter Lab
3. Rstudio

## Monitor resource usage

In the command line, type

```
htop
```