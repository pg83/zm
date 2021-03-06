module: library

#if OS_LINUX and not MUSL
ld_flags:
- -lutil
- -lrt
- -lcrypt
#endif

#if OS_DARWIN
framework:
- CoreFoundation
- SystemConfiguration
#endif

depends:
- tp/libs/expat
- tp/libs/bz2
- tp/libs/openssl
- tp/libs/z
- tp/libs/mpdec
- tp/libs/lzma
- tp/libs/python/src/Modules/_sqlite

inc_dirs:
- tp/libs/expat
- tp/libs/bz2
- tp/libs/openssl
- tp/libs/z
- tp/libs/mpdec
- tp/libs/lzma/api
- tp/libs/python/src/Include
- tp/libs/python/src/Include/internal
- tp/libs/python/src/Modules

c_flags:
- -DPy_BUILD_CORE_MODULE
- -DPREFIX="/var/empty"
- -DEXEC_PREFIX="/var/empty"
- -DPYTHONPATH="/var/empty"
- -DVERSION="3.9"
- -DVPATH=""
- -w

srcs:
- _abc.c
- _asynciomodule.c
- _bisectmodule.c
- _blake2/blake2b_impl.c
- _blake2/blake2module.c
- _blake2/blake2s_impl.c
- _blake2/impl/blake2-dispatch.c
- _blake2/impl/blake2b-ref.c
- _blake2/impl/blake2b.c
- _blake2/impl/blake2bp.c
- _blake2/impl/blake2s-ref.c
- _blake2/impl/blake2s.c
- _blake2/impl/blake2sp.c
- _bz2module.c
- _codecsmodule.c
- _collectionsmodule.c
- _contextvarsmodule.c
- _cryptmodule.c
- _csv.c
#if CTYPES
- _ctypes/_ctypes.c
- _ctypes/_ctypes_test.c
- _ctypes/callbacks.c
- _ctypes/callproc.c
- _ctypes/cfield.c
- _ctypes/darwin/README.ctypes
- _ctypes/darwin/dlfcn_simple.c
- _ctypes/libffi_osx/ffi.c
- _ctypes/libffi_osx/powerpc/ppc-ffi_darwin.c
- _ctypes/libffi_osx/types.c
- _ctypes/libffi_osx/x86/x86-ffi64.c
- _ctypes/libffi_osx/x86/x86-ffi_darwin.c
- _ctypes/malloc_closure.c
- _ctypes/stgdict.c
#endif
- _datetimemodule.c
- _decimal/_decimal.c
- _elementtree.c
- _functoolsmodule.c
#- _gdbmmodule.c
- _hashopenssl.c
- _heapqmodule.c
- _io/_iomodule.c
- _io/bufferedio.c
- _io/bytesio.c
- _io/fileio.c
- _io/iobase.c
- _io/stringio.c
- _io/textio.c
- _io/winconsoleio.c
- _json.c
#- _localemodule.c
- _lsprof.c
- _lzmamodule.c
- _math.c
- _multiprocessing/multiprocessing.c
- _multiprocessing/posixshmem.c
- _multiprocessing/semaphore.c
- _opcode.c
- _operator.c
- _peg_parser.c
- _pickle.c
- _posixsubprocess.c
- _queuemodule.c
- _randommodule.c
#if OS_DARWIN
#- _scproxy.c
#endif
- _sha3/sha3module.c
- _sre.c
- _ssl.c
- _stat.c
- _statisticsmodule.c
- _struct.c
- _testbuffer.c
- _testcapimodule.c
- _testimportmultiple.c
- _testinternalcapi.c
- _testmultiphase.c
- _threadmodule.c
- _tracemalloc.c
#- _uuidmodule.c
- _weakref.c
- _xxsubinterpretersmodule.c
- _xxtestfuzz/_xxtestfuzz.c
- _xxtestfuzz/fuzzer.c
- _zoneinfo.c
- arraymodule.c
- atexitmodule.c
- audioop.c
- binascii.c
- cjkcodecs/_codecs_cn.c
- cjkcodecs/_codecs_hk.c
- cjkcodecs/_codecs_iso2022.c
- cjkcodecs/_codecs_jp.c
- cjkcodecs/_codecs_kr.c
- cjkcodecs/_codecs_tw.c
- cjkcodecs/multibytecodec.c
- cmathmodule.c
- config.c
- errnomodule.c
- faulthandler.c
- fcntlmodule.c
- gcmodule.c
- getbuildinfo.c
- getpath.c
- grpmodule.c
- itertoolsmodule.c
- main.c
- mathmodule.c
- md5module.c
- mmapmodule.c
#- nismodule.c
- parsermodule.c
- posixmodule.c
- pwdmodule.c
- pyexpat.c
#- readline.c
- resource.c
- rotatingtree.c
- selectmodule.c
- sha1module.c
- sha256module.c
- sha512module.c
- signalmodule.c
- socketmodule.c
#if OS_LINUX
- spwdmodule.c
#endif
- symtablemodule.c
- syslogmodule.c
- termios.c
- timemodule.c
- unicodedata.c
- xxlimited.c
- xxmodule.c
- xxsubtype.c
- zlibmodule.c
