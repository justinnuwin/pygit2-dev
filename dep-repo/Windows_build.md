# Pygit2 Windows Build Instructions

# Requirements

- CMake (v2.8+ <- libgit2)
- MinGW necessary for openssl and ssh support
- Visual Studio (MSVC and Linker - Tested with Visual Studio 2017)


## Initial Setup

`LIBGIT2` environmental variable must be exported to some path


## Compile libgit2 native indows:

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

## Build Pygit2 (development version - MinGW) -- NOT WORKING (unable to correctly load CPython module)

From the pygit2 repo:

```bash
$ export CPATH="$CPATH:$HOME/Git/libgit2/include:/d/Justin/Git/libgit2/include"
$ export LIBRARY_PATH="$LIBRARY_PATH:/mingw64/lib:/mingw32/lib:$HOME/Git/libgit2/build"
$ python setup.py build
$ python setup.py install
```
