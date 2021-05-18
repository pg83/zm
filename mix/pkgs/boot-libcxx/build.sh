$untar $src/libcxx* && cd libcxx*

CXXFLAGS="$CPPFLAGS -DNDEBUG -D_LIBCPP_BUILDING_LIBRARY -D_LIBCPP_HAS_NO_PRAGMA_SYSTEM_HEADER -iquote src -I$out/include -DLIBCXXRT -std=c++14 -nostdinc++ -fvisibility-inlines-hidden $CXXFLAGS"

mkdir obj

cat << EOF > obj/__config
#if !defined(uiygfuiertyuiwetuyt)
#define uiygfuiertyuiwetuyt
#define _LIBCPP_HAS_MERGED_TYPEINFO_NAMES_DEFAULT 0
#endif
EOF

cat include/__config >> obj/__config && mv obj/__config include/ && cp -R include $out

SRCS1=$(ls src/*.cpp)
SRCS2=$(ls src/filesystem/*.cpp)

(
for s in $SRCS1 $SRCS2; do
    out=$(echo $s | tr '/' '_' | tr -d '\n').o
    g++ $CXXFLAGS -c $s -o obj/$out
done
)

ar q obj/libc++.a obj/*.o
ranlib obj/libc++.a

mkdir $out/lib && mv obj/libc++.a $out/lib/

cat << EOF > $out/env
export CPPFLAGS="-I$out/include \$CPPFLAGS"
export LIBS="$out/lib/libc++.a \$LIBS"
EOF
