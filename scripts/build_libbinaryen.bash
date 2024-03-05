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

arch=$(uname -m)
lib_path="./binaryen/libbinaryen/$arch-$platform/"
file="binaryen-version_$BINARYEN_VERSION-$arch-$platform.tar.gz"
url="https://github.com/WebAssembly/binaryen/releases/download/version_$BINARYEN_VERSION/$file"

mkdir -p $lib_path
wget -nc --no-check-certificate --content-disposition $url -P $lib_path
tar -xzvf $lib_path$file -C $lib_path --strip-components=1 --wildcards \
    "binaryen-version_$BINARYEN_VERSION/include/binaryen-c.h" \
    "binaryen-version_$BINARYEN_VERSION/include/wasm-delegations.def" \
    "binaryen-version_$BINARYEN_VERSION/lib/*"

echo "Running python script"
python3 ./scripts/create_cdef.py
