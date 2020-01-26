# IMSE 8410 Tools

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop. Source code
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Tools

This class is approached from two directions.  Concepts and Tools.  It
takes a tool-first approach not because they are more important, they
are only a means to an end, but because the technical constraints,
prerequisites, and the shear time it takes to absorb and use the tools
had to be carefully constructed.  The tools are used to apply concepts
and techniques.  We will always try to motivate and explain the "why"
of the tools but it takes active participation and thinking. The tools
are replaceable, the concepts and techniques endure.

### OnDemand

The first tool is a web interface to the Teaching Cluster (Clark) that
will be used throughout the class.  The web interface can be used for
the entire class but native ssh clients may be preferable (MobaXterm
for example in windows).  This interface provides a gateway to other
interactive and CLI services on Clark.  This list is always expanding
and please remember that this service is in Beta and to report any
issues that you may encounter.

Currently the Teaching Cluster provides the following via Open OnDemand:
 * A console (OnDemand) to manage interactive sessions with the cluster. https://openondemand.org/ 
 * A web based Secure Shell client to connect directly to the cluster. https://hterm.org/
 * Jupyter Lab and Jupyter Notebook environments for scientifc notebooks. https://jupyterlab.readthedocs.io/en/stable/
 * Web based RStudio Server for R. https://rstudio.com/products/rstudio/#rstudio-server
 * Web based Visual Studio Code IDE for advanced editing. https://github.com/Microsoft/vscode

To setup the OnDemand Jupyter Lab environment complete the steps
detailed in the following screenshots:

Navigate to https://ondemand.rnet.missouri.edu and Login.  `Click
Interactive Apps`.
![OnDemand](resources/OnDemand-01-Main.png "Click Interactive") `Click
Jupyter
Lab`
![OnDemand Jupyter Lab Setup](resources/OnDemand-02-Interactive_LI.jpg "Click Jupyter Lab") `Scroll
Down`
![OnDemand Jupyter Lab Setup](resources/OnDemand-03-NewLab.png "Scroll Down") `Change
Settings: Select 'Include Bash Kernel', 2 Hours, 2 Cores, 2 GB`; `Click
Launch`
![OnDemand Jupyter Lab Setup](resources/OnDemand-04-NewLabSettings_LI.jpg "Change Settings") Wait
20 or more
minutes.  While waiting you may wish to setup the Clark Shell (CLI) environment detailed in the next section.
![OnDemand Jupyter Lab Setup](resources/OnDemand-05-Wait.png "Wait 20 min") `Connect
to
Jupyter`
![OnDemand Jupyter Lab Setup](resources/OnDemand-08-Connect_LI.jpg "Click Connect to Jupyter") Jupyter
Lab
![OnDemand Jupyter Lab](resources/OnDemand-09-JupyterLab.png "Enjoy")

### Clark Shell (CLI)

A Command Line Interface (CLI), or terminal, is a way of interacting
with a system and dates back to the earliest of computing
machines. Commands are entered on a keyboard, the computer computes,
and the results are displayed. Although this method requires very low
bandwith to communicate to a machine, it provides the highest
"connection" with the machine.

A Secure Shell (ssh) session will be the primary way to access and
interact with the Clark Teaching Cluster during the semester and
should be used when ever possible.  Use of the OnDemand and Jupyter
Lab file management capabilities will only make it more difficult in
the long run to use the system.  We will now go over how to setup the
OnDemand.  There are detailed instructions below followed by a screen
capture of an example session.  Please be sure to replace login
information with your own.

To setup the Shell go to https://ondemand.rnet.missouri.edu and
navigate to `Clusters` > `_Clark Shell Access` or use the direct URL https://ondemand.rnet.missouri.edu/pun/sys/shell/ssh/clark.rnet.missouri.edu and complete the following:
 * If asked `Are you sure you want to continue connecting (yes/no)?`
   answer `yes` (just `y` will not work).
 * You should see a password prompt with your Pawprint in the beginning.
 ```
middelkoopt@clark.rnet.missouri.edu's password: 
 ```
 * Enter your University (Pawprint) password when prompted. 
   * You will not see anything while you type. If you do, stop. Something is wrong.
   * Press enter when you are done entering your password.
 * You should be greeted with the Message of the Day (MOTD) and a
 "Prompt". Your username should be seen just before the `@` followed
 by the name of the machine (hostname).
 ``` 
[middelkoopt@clark-r630-login-node907 ~]$
```

The setup of the shell is complete.  We will now generate a secure
shell key to allow for easier access to the system and to allow access
for other tools (GitLab).
 * Create a new *ssh key* by entering the command `ssh-keygen`
 * Press *enter* to accept the default location (`~/.ssh/id_rsa`)
 * Press *enter* to enter an empty pass phrase. (this is a machine key only)
 * Press *enter* to re-enter an empty pass phrase.
```
[middelkoopt@clark-r630-login-node907 ~]$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/middelkoopt/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/middelkoopt/.ssh/id_rsa.
Your public key has been saved in /home/middelkoopt/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:iZhVMCA+eDhljPMKa8pKJNlY3XbJjxAkwVr5FzFgEQg middelkoopt@clark-r630-login-node907
The key's randomart image is:
+---[RSA 2048]----+
| oEo+*X=+.       |
|o*.o=+ =.o       |
|+o=o..= +.       |
|.Bo. =.+.+       |
|=+. o ..S .      |
|=.               |
|+.               |
|o.               |
|o                |
+----[SHA256]-----+

```
Please note the "randomart" is *not* your ssh key.

We now need to allow access to Clark by OnDemand by adding the public key of the newly created key to the `.ssh/authorized_keys` file.
 * Copy the secure shell public key to the `authorized_keys` file in the `.ssh/` folder
 ```
cp -v .ssh/id_rsa.pub .ssh/authorized_keys
 ```
 * Secure the file by changing the permissions to be only readable and writable by your user.
 ```
chmod 600 .ssh/authorized_keys
 ```

The complete session:
```
[middelkoopt@clark-r630-login-node907 ~]$ cp -v .ssh/id_rsa.pub .ssh/authorized_keys
‘.ssh/id_rsa.pub’ -> ‘.ssh/authorized_keys’
[middelkoopt@clark-r630-login-node907 ~]$ chmod 600 .ssh/authorized_keys
[middelkoopt@clark-r630-login-node907 ~]$
```

A screen capture of the above directions can be seen below.

`Clusters > _Clark Shell Access`
![OnDemand Shell](resources/OnDemand-06-Clark.png "Launch Clark Shell")
![OnDemand Shell Setup](resources/OnDemand-07-CLI_LI.jpg "Enter Commands")
![OnDemand Shell Setup](resources/OnDemand-07-CLI.png "Commands")

### Gitlab

### Canvas (Assignments)

