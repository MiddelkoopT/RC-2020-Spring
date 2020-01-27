# ReadMe

This folder contains some generalized examples that can be used
outside the context of this class. They may need to be altered based
on the environment.

## Bash Bootstrap

Many envrionments do not have a Bash kernel.  To setup a bash kernel
run the following in a shell: 

```
bash conda install -y bash_kernel
python -m bash_kernel.install
```

If a conda envronment is not setup then use `pip install` instead of
`conda install`

