# Pygit2 Windows Build Instructions

Sample scripts which build libgit2 and pygit2 natively for Windows are provided in `scripts/`.

## Requirements

- CMake (v2.8+ <- libgit2)
- MinGW necessary for openssl and ssh support
- Visual Studio (MSVC and Linker - Tested with Visual Studio 2017)


## Initial Setup

`LIBGIT2` environmental variable must be exported to some path


## Compile libgit2 native Windows:

```bash
PS> cmake .. -DBUILD_CLAR=OFF -DTHREADSAFE=ON -DCMAKE_LIBRARY_PATH="path\to\mingw64\lib" -DUSE_SSH=OFF -DCMAKE_INSTALL_PREFIX=$Env:LIBGIT2  # -DBUILD_SHARED_LIBS=OFF
PS> cmake --build . --target install
```


## Compile libgit2 MinGW 

```bash
$ cmake .. -G "MinGW Makefiles" -DBUILD_CLAR=OFF -DTHREADSAFE=ON -DCMAKE_LIBRARY_PATH="/mingw64/lib" -DUSE_SSH=OFF -DCMAKE_INSTALL_PREFIX=$LIBGIT2  # -DBUILD_SHARED_LIBS=OFF
$ cmake --build . --target install
```


## Build Pygit2 (release version)

```bash
pip3 install pygit2   # Or alternatively install via Pycharm
```


## Build Pygit2 (development version - native windows)

1. Set `PATH` environmental variable to $LIBGIT2/bin
2. Set `INCLUDE` environmental variable to $LIBGIT2/include
3. Set `LIB` environmental variable to $LIBGIT2/lib
4. Launch a new Powershell session and navigate to pygit2 repo

```bash
PS> python setup.py build
PS> python setup.py install
```

Note that if the user does not have admin access, the `--user` flag needs to be appended to the `install` command to install the module to the user's `site-packages`.

Run the test, `backend.py` script. If you get the following error:

```
Traceback (most recent call last):
  File "C:\Users\nguyen104\pygit2-dev\backend.py", line 1, in <module>
    import pygit2
  File "C:\Users\nguyen104\AppData\Roaming\Python\Python39\site-packages\pygit2-1.6.1-py3.9-win-amd64.egg\pygit2\__init__.py", line 30, in <module>
    from ._pygit2 import *
ImportError: DLL load failed while importing _pygit2: The specified module could not be found.
```

Copy `git2.dll` in `dep-repo\build\bin\` to where the module was installed to.

You can determine where the module was installed by looking at the output from the above install command (you sould see a line reading): `Installed c:\users\nguyen104\appdata\roaming\python\python39\site-packages\pygit2-1.6.1-py3.9-win-amd64.egg`

Copy the dll:

`cp dep-repo\build\bin\git2.dll c:\users\nguyen104\appdata\roaming\python\python39\site-packages\pygit2-1.6.1-py3.9-win-amd64.egg\pygit2`

## Build Pygit2 (development version - MinGW) -- NOT WORKING (unable to correctly load CPython module)

From the pygit2 repo:

```bash
$ export CPATH="$CPATH:$HOME/Git/libgit2/include:/d/Justin/Git/libgit2/include"
$ export LIBRARY_PATH="$LIBRARY_PATH:/mingw64/lib:/mingw32/lib:$HOME/Git/libgit2/build"
$ python setup.py build
$ python setup.py install
```
