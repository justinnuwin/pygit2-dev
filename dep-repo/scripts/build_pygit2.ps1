# This script needs to be run from scripts/

Set-Location "..\pygit2"

# These paths relative to both pygit2/ and scripts/
$Env:PATH += ";..\build\bin"
$Env:INCLUDE = "..\build\include"
$Env:LIB = "..\build\lib"

python setup.py build_ext --inplace;