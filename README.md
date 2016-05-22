# README

FIXME : description

## Scripts

### test_suite.py

```
$ test_suite.py (or python2.7 test_suite.py) [folders]
```

* Each folder is a categorie, must contain one file per test.

* Test file format :

```
TITLE
Example

COMMAND
diff out1 out2

stderr:
error

stdout:
everything is ok

RETURN
0
```


### doc_func.py

* Doxygen documentation for all files with <extension> in subdirectories :

```
$ doc_func.py <extension>
```


### beep (requires root privileges)

* System beep enabling :

```
$ beep start
```

* System beep disabling :

```
$ beep stop
```


### restart_mouse (requires root privileges)

* Restarting mouse :

```
$ restart_mouse
```


## Sources

### libargs

* The simplest option manager for C++ : retrieve a map which, for any argument gave its position, 0 if it doesn't exist.

* Usage :

```
Args args(int argc, char** argv);

args.push_arg(arg1);
...

args.compute();
args.map_get();
```


### demonizer

FIXME : submodule


## Dotfiles

FIXME


## Install

```
sudo PREFIX=... MAN=...  ./install.sh
```

* PREFIX : install directory

* MAN : package manager

* Default : MAN=apt-get, PREFIX=/usr/local
