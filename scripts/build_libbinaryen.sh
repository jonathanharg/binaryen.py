#!/bin/bash

case "$(uname -sr)" in

Darwin*)
    platform='macos'
    ;;

Linux*)
    platform='linux'
    ;;

CYGWIN* | MINGW* | MINGW32* | MSYS*)
    platform='windows'
    ;;

*)
    echo 'Other OS detected' 1>&2
    exit 1
    ;;
esac

if [ -z ${BINARYEN_VERSION+x} ]
then
    echo "\$BINARYVEN_VERSION not set"
    exit 1
fi

wildcards="--wildcards"

if [[ "$platform" == "macos" ]]
then
    wildcards=""
fi

arch=$(uname -m)
lib_path="./binaryen/libbinaryen/$arch-$platform/"
mkdir -p $lib_path

if [[ "$platform" == "macos" ]]
then
    mkdir -p "./binaryen/libbinaryen/src/"
    file="version_$BINARYEN_VERSION.tar.gz"
    url="https://github.com/WebAssembly/binaryen/archive/refs/tags/$file"
    wget -nc --no-check-certificate --content-disposition $url -P "./binaryen/libbinaryen"
    tar -xzvf "./binaryen/libbinaryen/binaryen-$file" -C "./binaryen/libbinaryen/src" --strip-components=1
    cmake -S "./binaryen/libbinaryen/src" -B "./binaryen/libbinaryen/build/" -G Ninja \
        -DCMAKE_INSTALL_PREFIX="$lib_path" -DCMAKE_OSX_ARCHITECTURES=$arch \
        -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF \
        -DBUILD_STATIC_LIB=ON
    cmake --build "./binaryen/libbinaryen/build/" -v --config Release --target install
else
    file="binaryen-version_$BINARYEN_VERSION-$arch-$platform.tar.gz"
    url="https://github.com/WebAssembly/binaryen/releases/download/version_$BINARYEN_VERSION/$file"
    wget -nc --no-check-certificate --content-disposition $url -P $lib_path
    tar -xzvf $lib_path$file -C $lib_path --strip-components=1 $wildcards \
        "binaryen-version_$BINARYEN_VERSION/include/binaryen-c.h" \
        "binaryen-version_$BINARYEN_VERSION/include/wasm-delegations.def" \
        "binaryen-version_$BINARYEN_VERSION/lib/*"
fi

echo "Running python script"
python3 ./scripts/create_cdef.py
