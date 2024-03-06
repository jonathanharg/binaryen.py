#!/bin/bash

arch=$(uname -m)

case "$(uname -sr)" in

Darwin*)
    platform='macos'
    ;;

Linux*)
    platform='linux'
    ;;

CYGWIN* | MINGW* | MINGW32* | MSYS*)
    platform='windows'
    if [[ "$arch" == "amd-64" ]]; then
        arch="x86_64"
    fi
    ;;

*)
    echo 'Other OS detected' 1>&2
    exit 1
    ;;
esac

if [ -z ${BINARYEN_VERSION+x} ]; then
    echo "\$BINARYVEN_VERSION not set"
    exit 1
fi

lib_path="./binaryen/libbinaryen/$arch-$platform"
mkdir -p $lib_path

if grep -Fxq $BINARYEN_VERSION $lib_path/version; then
    # Existing version found
    echo "Found existing binaryen installation, skipping."
    echo "You may need to clear the binaryen/libbinaryen folder if errors occur"
    exit 0
fi

wildcards="--wildcards"

if [[ "$platform" == "macos" ]]; then
    wildcards=""
fi

echo "Setting up binaryen for $arch $platform"

if [[ "$platform" == "macos" ]]; then
    echo "Building static binaryen for MacOS"
    mkdir -p "./binaryen/libbinaryen/src/"

    file="version_$BINARYEN_VERSION.tar.gz"
    url="https://github.com/WebAssembly/binaryen/archive/refs/tags/$file"

    wget -q -nc --no-check-certificate --content-disposition $url -P "./binaryen/libbinaryen"
    echo "Downloaded source code"

    tar -xzf "./binaryen/libbinaryen/binaryen-$file" -C "./binaryen/libbinaryen/src" --strip-components=1
    echo "Extracted source code"

    cmake -S "./binaryen/libbinaryen/src" -B "./binaryen/libbinaryen/build/" -G Ninja \
        -DCMAKE_INSTALL_PREFIX="$lib_path" -DCMAKE_OSX_ARCHITECTURES=$arch \
        -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF \
        -DBUILD_STATIC_LIB=ON
    cmake --build "./binaryen/libbinaryen/build/" -v --config Release --target install
else
    file="binaryen-version_$BINARYEN_VERSION-$arch-$platform.tar.gz"
    url="https://github.com/WebAssembly/binaryen/releases/download/version_$BINARYEN_VERSION/$file"

    wget -q -nc --no-check-certificate --content-disposition $url -P $lib_path
    echo "Downloaded release $BINARYEN_VERSION"
    
    tar -xzf $lib_path/$file -C $lib_path --strip-components=1 $wildcards \
        "binaryen-version_$BINARYEN_VERSION/include/binaryen-c.h" \
        "binaryen-version_$BINARYEN_VERSION/include/wasm-delegations.def" \
        "binaryen-version_$BINARYEN_VERSION/lib/*"
    echo "Extracted release"
fi

echo "Generating C def file"
python3 ./scripts/create_cdef.py
echo "Successfully generated C def file"

echo "$BINARYEN_VERSION" >| $lib_path/version