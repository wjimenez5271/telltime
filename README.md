# telltime

A simple CLI utility for working with epoch time.

### Install

```
python setup.py install
```

The command `epoch` should now be available in your path.

### Usage
Convert an epoch time stamp to human readable

```
$ epoch 1456208958
2016-02-22T22:29:18
```

Get current time in epoch

```
$ epoch
Current epoch time: 1456208958.19
```

### Requirements
Tested on python 2.7. Requires `argparse`.