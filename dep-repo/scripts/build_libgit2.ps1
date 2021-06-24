# This script needs to be run from scripts/

rm "..\build"
mkdir "..\build"    # libgit2 installation prefix

Set-Location "..\libgit2"
rm "build"
mkdir build
Set-Location "build"

cmake .. -DBUILD_CLAR=OFF -DTHREADSAFE=ON -DCMAKE_LIBRARY_PATH="path\to\mingw64\lib" -DUSE_SSH=OFF -DCMAKE_INSTALL_PREFIX="..\..\build"  # -DBUILD_SHARED_LIBS=OFF
cmake --build . --target install