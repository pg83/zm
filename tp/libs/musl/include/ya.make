# Generated by devtools/yamaker.

LIBRARY()

OWNER(heretic g:cpp-contrib vladon)

LICENSE(MIT)

ADDINCL(
    GLOBAL contrib/libs/musl/arch/x86_64
    GLOBAL contrib/libs/musl/arch/generic
    GLOBAL contrib/libs/musl/include
    GLOBAL contrib/libs/musl/extra
)

NO_PLATFORM()

NO_RUNTIME()

END()
