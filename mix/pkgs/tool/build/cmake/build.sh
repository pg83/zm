$untar $src/cmake* && cd cmake*

export CPPFLAGS="-w $CPPFLAGS"

build_cmake_ninja \
    -DCMAKE_USE_OPENSSL=OFF \
    -Dfortran=OFF \
    -DBUILD_TESTING=OFF \
    -DCMAKE_USE_SYSTEM_LIBARCHIVE=ON \
    -DCMAKE_USE_SYSTEM_EXPAT=ON \
    -DCMAKE_USE_SYSTEM_ZLIB=ON \
    -DCMAKE_USE_SYSTEM_BZIP2=ON \
    -DCMAKE_USE_SYSTEM_LIBLZMA=ON \
    -DCMAKE_USE_SYSTEM_ZSTD=OFF \
    -DZLIB_LIBRARY="$lib_z/lib/libz.a" \
    -DZLIB_INCLUDE_DIR="$lib_z/include" \
    -DEXPAT_LIBRARY="$lib_expat/lib/libexpat.a" \
    -DEXPAT_INCLUDE_DIR="$lib_expat/include" \
    -DLibArchive_LIBRARY="$lib_archive/lib/libarchive.a" \
    -DLibArchive_INCLUDE_DIR="$lib_archive/include" \
    ..
