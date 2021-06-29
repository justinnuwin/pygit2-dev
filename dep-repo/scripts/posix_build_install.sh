#!/bin/bash

# Ensure that CWD is scripts/
# If pygit2 is to be installed in a virtual environment, make sure the venv is activated before running
pushd ..
LIBGIT2=$(pwd)/build
mkdir -p $LIBGIT2

git submodule update --init

mkdir -p libgit2/build
pushd libgit2/build
cmake .. -DCMAKE_INSTALL_PREFIX=$LIBGIT2 -DUSE_SSH=ON -DBUILD_CLAR=OFF
cmake --build . --target install
popd

pushd pygit2
CPATH=$LIBGIT2/include LIBRARY_PATH=$LIBGIT2/lib* CFLAGS="-O0 -g -std=c11" python3 build_ext --inplace
python3 install
popd

popd