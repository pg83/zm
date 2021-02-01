#include "Python.h"

extern PyObject* PyInit__abc();
extern PyObject* PyInit__ast();
extern PyObject* PyInit__asyncio();
extern PyObject* PyInit__bisect();
extern PyObject* PyInit__blake2();
extern PyObject* PyInit__bz2();
extern PyObject* PyInit__codecs();
extern PyObject* PyInit__collections();
extern PyObject* PyInit__contextvars();
extern PyObject* PyInit__crypt();
extern PyObject* PyInit__csv();
extern PyObject* PyInit__datetime();
extern PyObject* PyInit__decimal();
extern PyObject* PyInit__elementtree();
extern PyObject* PyInit__functools();
extern PyObject* PyInit__hashlib();
extern PyObject* PyInit__heapq();
extern PyObject* PyInit__imp();
extern PyObject* PyInit__io();
extern PyObject* PyInit__json();
extern PyObject* PyInit__lsprof();
extern PyObject* PyInit__lzma();
extern PyObject* PyInit__md5();
extern PyObject* PyInit__multibytecodec();
extern PyObject* PyInit__multiprocessing();
extern PyObject* PyInit__opcode();
extern PyObject* PyInit__operator();
#if defined(_MSC_VER)
extern PyObject* PyInit__overlapped();
#endif
extern PyObject* PyInit__peg_parser();
extern PyObject* PyInit__pickle();
extern PyObject* PyInit__posixshmem();
extern PyObject* PyInit__posixsubprocess();
extern PyObject* PyInit__queue();
extern PyObject* PyInit__random();
#if defined(__APPLE__)
extern PyObject* PyInit__scproxy();
#endif
extern PyObject* PyInit__sha1();
extern PyObject* PyInit__sha256();
extern PyObject* PyInit__sha3();
extern PyObject* PyInit__sha512();
extern PyObject* PyInit__signal();
extern PyObject* PyInit__socket();
extern PyObject* PyInit__sre();
extern PyObject* PyInit__ssl();
extern PyObject* PyInit__stat();
extern PyObject* PyInit__statistics();
extern PyObject* PyInit__string();
extern PyObject* PyInit__struct();
extern PyObject* PyInit__symtable();
extern PyObject* PyInit__thread();
extern PyObject* PyInit__tracemalloc();
extern PyObject* PyInit__weakref();
#if defined(_MSC_VER)
extern PyObject* PyInit__winapi();
#endif
extern PyObject* PyInit__xxsubinterpreters();
extern PyObject* PyInit__zoneinfo();
extern PyObject* PyInit_array();
extern PyObject* PyInit_atexit();
extern PyObject* PyInit_audioop();
extern PyObject* PyInit_binascii();
extern PyObject* PyInit_cmath();
extern PyObject* PyInit_errno();
extern PyObject* PyInit_faulthandler();
extern PyObject* PyInit_fcntl();
extern PyObject* PyInit_gc();
extern PyObject* PyInit_grp();
extern PyObject* PyInit_itertools();
extern PyObject* PyInit_math();
extern PyObject* PyInit_mmap();
extern PyObject* PyInit_parser();
extern PyObject* PyInit_posix();
extern PyObject* PyInit_pwd();
extern PyObject* PyInit_resource();
extern PyObject* PyInit_select();
#if defined(__linux__)
extern PyObject* PyInit_spwd();
#endif
extern PyObject* PyInit_syslog();
extern PyObject* PyInit_termios();
extern PyObject* PyInit_time();
extern PyObject* PyInit_unicodedata();
extern PyObject* PyInit_xx();
extern PyObject* PyInit_xxlimited();
extern PyObject* PyInit_xxsubtype();
extern PyObject* PyInit_zlib();
extern PyObject* PyMarshal_Init(void);
extern PyObject* _PyWarnings_Init(void);

struct _inittab _PyImport_Inittab[] = {
    {"_abc", PyInit__abc},
    {"_ast", PyInit__ast},
    {"_asyncio", PyInit__asyncio},
    {"_bisect", PyInit__bisect},
    {"_blake2", PyInit__blake2},
    {"_bz2", PyInit__bz2},
    {"_codecs", PyInit__codecs},
    {"_collections", PyInit__collections},
    {"_contextvars", PyInit__contextvars},
    {"_crypt", PyInit__crypt},
    {"_csv", PyInit__csv},
    {"_datetime", PyInit__datetime},
    {"_decimal", PyInit__decimal},
    {"_elementtree", PyInit__elementtree},
    {"_functools", PyInit__functools},
    {"_hashlib", PyInit__hashlib},
    {"_heapq", PyInit__heapq},
    {"_imp", PyInit__imp},
    {"_io", PyInit__io},
    {"_json", PyInit__json},
    {"_lsprof", PyInit__lsprof},
    {"_lzma", PyInit__lzma},
    {"_md5", PyInit__md5},
    {"_multibytecodec", PyInit__multibytecodec},
    {"_multiprocessing", PyInit__multiprocessing},
    {"_opcode", PyInit__opcode},
    {"_operator", PyInit__operator},
#if defined(_MSC_VER)
    {"_overlapped", PyInit__overlapped},
#endif
    {"_peg_parser", PyInit__peg_parser},
    {"_pickle", PyInit__pickle},
    {"_posixshmem", PyInit__posixshmem},
    {"_posixsubprocess", PyInit__posixsubprocess},
    {"_queue", PyInit__queue},
    {"_random", PyInit__random},
#if defined(__APPLE__)
    {"_scproxy", PyInit__scproxy},
#endif
    {"_sha1", PyInit__sha1},
    {"_sha256", PyInit__sha256},
    {"_sha3", PyInit__sha3},
    {"_sha512", PyInit__sha512},
    {"_signal", PyInit__signal},
    {"_socket", PyInit__socket},
    {"_sre", PyInit__sre},
    {"_ssl", PyInit__ssl},
    {"_stat", PyInit__stat},
    {"_statistics", PyInit__statistics},
    {"_string", PyInit__string},
    {"_struct", PyInit__struct},
    {"_symtable", PyInit__symtable},
    {"_thread", PyInit__thread},
    {"_tracemalloc", PyInit__tracemalloc},
    {"_weakref", PyInit__weakref},
#if defined(_MSC_VER)
    {"_winapi", PyInit__winapi},
#endif
    {"_xxsubinterpreters", PyInit__xxsubinterpreters},
    {"_zoneinfo", PyInit__zoneinfo},
    {"array", PyInit_array},
    {"atexit", PyInit_atexit},
    {"audioop", PyInit_audioop},
    {"binascii", PyInit_binascii},
    {"cmath", PyInit_cmath},
    {"errno", PyInit_errno},
    {"faulthandler", PyInit_faulthandler},
    {"fcntl", PyInit_fcntl},
    {"gc", PyInit_gc},
    {"grp", PyInit_grp},
    {"itertools", PyInit_itertools},
    {"math", PyInit_math},
    {"mmap", PyInit_mmap},
    {"parser", PyInit_parser},
    {"posix", PyInit_posix},
    {"pwd", PyInit_pwd},
    {"resource", PyInit_resource},
    {"select", PyInit_select},
#if defined(__linux__)
    {"spwd", PyInit_spwd},
#endif
    {"syslog", PyInit_syslog},
    {"termios", PyInit_termios},
    {"time", PyInit_time},
    {"unicodedata", PyInit_unicodedata},
    {"xx", PyInit_xx},
    {"xxlimited", PyInit_xxlimited},
    {"xxsubtype", PyInit_xxsubtype},
    {"zlib", PyInit_zlib},
    {"marshal", PyMarshal_Init},
    {"_warnings", _PyWarnings_Init},
    {"builtins", NULL},
    {"sys", NULL},
    {0, 0}
};
