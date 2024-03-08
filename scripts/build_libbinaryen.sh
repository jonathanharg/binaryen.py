#!/bin/bash
root_path="./binaryen/libbinaryen"

if grep -Fxq $BINARYEN_VERSION $root_path/version; then
    # Existing version found
    echo "Found existing binaryen installation, skipping."
    echo "You may need to clear the binaryen/libbinaryen folder if errors occur"
    exit 0
fi

arch=$(uname -m)

# Set the platform = 'macos' | 'linux' | 'windows'
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

lib_path="$root_path/$arch-$platform"
mkdir -p $lib_path

wildcards="--wildcards"

if [[ "$platform" == "macos" ]]; then
    # Wildcards are supported by default on macOS
    wildcards=""
fi

echo "Setting up binaryen for $arch $platform"

if [[ "$platform" == "macos" ]]; then
    echo "Building static binaryen for macOS"
    mkdir -p "$root_path/src/"

    file="version_$BINARYEN_VERSION.tar.gz"
    url="https://github.com/WebAssembly/binaryen/archive/refs/tags/$file"

    wget -q -nc --no-check-certificate --content-disposition $url -P "$root_path"
    echo "Downloaded source code"

    tar -xzf "$root_path/binaryen-$file" -C "$root_path/src" --strip-components=1
    echo "Extracted source code"

    echo "Building for Apple Silicon"
    cmake -S "$root_path/src" -B "$root_path/build/" -G Ninja \
        -DCMAKE_INSTALL_PREFIX=""$root_path/arm64-macos"" -DCMAKE_OSX_ARCHITECTURES="arm64" \
        -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF \
        -DBUILD_STATIC_LIB=ON
    cmake --build "$root_path/build/" -v --config Release --target install

    echo "Build for Intel"
    cmake -S "$root_path/src" -B "$root_path/build/" -G Ninja \
        -DCMAKE_INSTALL_PREFIX=""$root_path/x86_64-macos"" -DCMAKE_OSX_ARCHITECTURES="x86_64" \
        -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF \
        -DBUILD_STATIC_LIB=ON
    cmake --build "$root_path/build/" -v --config Release --target install
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

echo "$BINARYEN_VERSION" >| $root_path/version