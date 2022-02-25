# CUIMC VPN

For general information see: https://www.it.cuimc.columbia.edu

This VPN is different from Columbia VPN. Columbia VPN will appear in your phone's Duo Mobile app as "Columbia University". This will appear as "CUMC".

## Setup Duo MFA for VPN access

You need to set up the CUIMC MFA (not Columbia MFA!) in order to use CUIMC VPN.
[Here are instructions](https://mfa.cumc.columbia.edu/content/how-enroll-cuimc-mfa).
Several options are available but it is perhaps most convenient to setup it to your cell phone with an app called "Duo Mobile".

Notice that the actual setup can only be performed outside of the CUIMC campus.

## Using CUIMC VPN with Duo MFA

### On Mac and Windows

Here are instructions [for Mac and Windows](https://mfa.cumc.columbia.edu/content/using-cuimc-vpn-duo-mfa). Briefly:

1. Active your Duo account: download the Duo app on your phone and get the duo authentication: https://cuit.columbia.edu/mfa.
2. Download and install the VPN client on your desktop --- Cisco AnyConnect VPN: https://cuit.columbia.edu/install-vpn.
3. Open AnyConnect and connect to `ssl.cpmc.columbia.edu` on AnyConnect with your UNI.

If you have any problem with CUMC VPN, please see more information here: https://www.it.cuimc.columbia.edu/

### On Linux

From the off-campus Linux computer:

```
sudo openconnect -u <UNI> -g CUMC-VPN ssl.cpmc.columbia.edu
```

where `<UNI>` is your Columbia UNI. `sudo` is required to run the VPN connection. You should have `sudo` privileges anyways for your own Linux computer.
The VPN client, `openconnect`, can be installed on Debian based Linux systems via `apt-get install openconnect`.

After entering the command you may be prompted to enter the `[sudo]` password. This is the password of your Linux user account. After that, `openconnect` will prompt you to enter a password which is your Columbia UNI password. Then it will again ask you for a password as if what you have previously entered did not work; but this time you have to type in "`push`" (without quote) and hit enter. This instructs a Duo authentication request to be sent. You will then receive a notification on the "Duo Mobile" app on your phone (or, Apple Watch) that you have to tap to authorize.
After that you'll be connected. Please keep the terminal open in order for the client to stay connected.

## Work with multiple HPC via different VPN network

Sometimes we need to work on different HPC in different network from the same computer. On Linux it is possible to connect to multiple VPN networks at the same time. 
On Mac, however, multiple VPNs through `openconnect` does not work (they conflict each other). 
A simple workaround is to run a docker container for every other VPN network you would like to connect, and connect from the container.

To do so, first pull a docker image we provide, which has `openconnect` and `openssh` client installed:

```
docker pull gaow/openconnect
```

Then run a docker container from the image (you can replace `your_choice_of_name` to any strings you like):

```
docker run -d --rm --security-opt label:disable --privileged -t -v $HOME/.ssh:/root/.ssh  --name your_choice_of_name gaow/openconnect
```

with `-v $HOME/.ssh:/root/.ssh` you will load SSH key of your computer to the docker instance, as if that docker instance is your computer. This is not necessary unless you use SSH key to access some cluster systems.

Finally, log into the docker container:

```
docker exec -it your_choice_of_name bash
```

Inside the container, run the openconnect command without `sudo`:

```
openconnect -u <UNI> -g CUMC-VPN ssl.cpmc.columbia.edu
```

See instructions in the previous section how to connect with `openconnect`. After you are connected, you need to send the openconnect process to the background so you can continue working with the terminal. To do so, press `ctrl-z`, then type:

```
bg
```

You should see something like below:

```
^Z
[1]+  Stopped                 openconnect -u gw2411 -g CUMC-VPN ssl.cpmc.columbia.edu
root@44d9189b41ae:/tmp# bg
[1]+ openconnect -u gw2411 -g CUMC-VPN ssl.cpmc.columbia.edu &
root@44d9189b41ae:/tmp# 
```

Now you can use the terminal to connect to the HPC on the VPN network. To stop the docker container after use:

```
docker stop your_choice_of_name
```

## Contact
Gao Wang and Haoyue Shuai
