$untar $src/v* && cd far*

export CPPFLAGS="-DPpmd8_RangeDec_Init=Ppmd8_RangeDec_InitXX -DPpmd8_Init=Ppmd8_InitXX -DPpmd8_Construct=Ppmd8_ConstructXX -DPpmd8_MakeEscFreq=Ppmd8_MakeEscFreqXX -DPpmd8_UpdateBin=Ppmd8_UpdateBinXX -DPpmd8_DecodeSymbol=Ppmd8_DecodeSymbolXX -DPPMD8_kExpEscape=PPMD8_kExpEscapeXX -DPpmd8_Free=Ppmd8_FreeXX -DPpmd8_Alloc=Ppmd8_AllocXX -DPpmd8_Update2=Ppmd8_Update2XX -DPpmd8_Update1=Ppmd8_Update1XX -DPpmd8_Update1_0=Ppmd8_Update1_0XX $CPPFLAGS"

build_cmake_ninja \
    -DUSEWX=no \
    -DUCHARDET_LIBRARY=$lib_uchardet/lib/libuchardet.a \
    -DUCHARDET_INCLUDE_DIR=$lib_uchardet/include/uchardet \
    -DSPDLOG_INCLUDE_DIR=$lib_spdlog/include \
    -DXERCESC_INCLUDE_DIR=$lib_xerces_c/include \
    ..
