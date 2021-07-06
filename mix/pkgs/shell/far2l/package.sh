# url https://github.com/elfmz/far2l/archive/b246b95118c0d7c6d10b4e94ec9b3bc7e24c3a7c.zip
# md5 26e676988fa5b47ed211281e6140d371
# dep lib/ssh lib/pcre lib/spdlog lib/archive lib/xerces-c lib/uchardet dev/build/pkg-config dev/build/cmake dev/lang/m4 stdenv

build() {
    $unzip $src/*.zip && cd far*

    export CPPFLAGS="-DPpmd8_RangeDec_Init=Ppmd8_RangeDec_InitXX -DPpmd8_Init=Ppmd8_InitXX -DPpmd8_Construct=Ppmd8_ConstructXX -DPpmd8_MakeEscFreq=Ppmd8_MakeEscFreqXX -DPpmd8_UpdateBin=Ppmd8_UpdateBinXX -DPpmd8_DecodeSymbol=Ppmd8_DecodeSymbolXX -DPPMD8_kExpEscape=PPMD8_kExpEscapeXX -DPpmd8_Free=Ppmd8_FreeXX -DPpmd8_Alloc=Ppmd8_AllocXX -DPpmd8_Update2=Ppmd8_Update2XX -DPpmd8_Update1=Ppmd8_Update1XX -DPpmd8_Update1_0=Ppmd8_Update1_0XX $CPPFLAGS"

    build_cmake_ninja -DUSEWX=no ..
}
