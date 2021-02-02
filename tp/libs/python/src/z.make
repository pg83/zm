module: library

depends:
- tp/libs/python/src/Modules

inc_dirs:
- tp/libs/python/src/Include
- tp/libs/python/src/Include/internal

global_inc_dirs:
- tp/libs/python/src/Include

c_flags:
- -DPLATLIBDIR="/var/empty"
- -DPy_BUILD_CORE
- -w

srcs:
- Objects/abstract.c
- Objects/accu.c
- Objects/boolobject.c
- Objects/bytearrayobject.c
- Objects/bytes_methods.c
- Objects/bytesobject.c
- Objects/call.c
- Objects/capsule.c
- Objects/cellobject.c
- Objects/classobject.c
- Objects/codeobject.c
- Objects/complexobject.c
- Objects/descrobject.c
- Objects/dictobject.c
- Objects/enumobject.c
- Objects/exceptions.c
- Objects/fileobject.c
- Objects/floatobject.c
- Objects/frameobject.c
- Objects/funcobject.c
- Objects/genericaliasobject.c
- Objects/genobject.c
- Objects/interpreteridobject.c
- Objects/iterobject.c
- Objects/listobject.c
- Objects/longobject.c
- Objects/memoryobject.c
- Objects/methodobject.c
- Objects/moduleobject.c
- Objects/namespaceobject.c
- Objects/object.c
- Objects/obmalloc.c
- Objects/odictobject.c
- Objects/picklebufobject.c
- Objects/rangeobject.c
- Objects/setobject.c
- Objects/sliceobject.c
- Objects/structseq.c
- Objects/tupleobject.c
- Objects/typeobject.c
- Objects/unicodectype.c
- Objects/unicodeobject.c
- Objects/weakrefobject.c
- Parser/acceler.c
- Parser/grammar1.c
- Parser/listnode.c
- Parser/myreadline.c
- Parser/node.c
- Parser/parser.c
- Parser/parsetok.c
- Parser/pegen/parse.c
- Parser/pegen/parse_string.c
- Parser/pegen/peg_api.c
- Parser/pegen/pegen.c
- Parser/token.c
- Parser/tokenizer.c
- Python/Python-ast.c
- Python/_warnings.c
- Python/asdl.c
- Python/ast.c
- Python/ast_opt.c
- Python/ast_unparse.c
- Python/bltinmodule.c
- Python/bootstrap_hash.c
- Python/ceval.c
- Python/codecs.c
- Python/compile.c
- Python/context.c
- Python/dtoa.c
- Python/dup2.c
- Python/dynamic_annotations.c
- Python/dynload_stub.c
- Python/errors.c
- Python/fileutils.c
- Python/formatter_unicode.c
- Python/frozen.c
- Python/frozenmain.c
- Python/future.c
- Python/getargs.c
- Python/getcompiler.c
- Python/getcopyright.c
- Python/getopt.c
- Python/getplatform.c
- Python/getversion.c
- Python/graminit.c
- Python/hamt.c
- Python/hashtable.c
- Python/import.c
- Python/importdl.c
- Python/initconfig.c
- Python/marshal.c
- Python/modsupport.c
- Python/mysnprintf.c
- Python/mystrtoul.c
- Python/pathconfig.c
- Python/peephole.c
- Python/preconfig.c
- Python/pyarena.c
- Python/pyctype.c
- Python/pyfpe.c
- Python/pyhash.c
- Python/pylifecycle.c
- Python/pymath.c
- Python/pystate.c
- Python/pystrcmp.c
- Python/pystrhex.c
- Python/pystrtod.c
- Python/pythonrun.c
- Python/pytime.c
- Python/structmember.c
- Python/symtable.c
- Python/sysmodule.c
- Python/thread.c
- Python/traceback.c
