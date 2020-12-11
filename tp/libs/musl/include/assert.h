#include <features.h>

#undef assert

#ifdef NDEBUG
#define	assert(x) (void)0
#else
#define assert(x) ((void)((x) || (__assert_fail(#x, __FILE__, __LINE__, __func__),0)))
#endif

#if __STDC_VERSION__ >= 201112L && !defined(__cplusplus)
#define static_assert _Static_assert
#endif

#if defined(__cplusplus) && defined(__NVCC__) && defined(__GNUC__)
extern "C" {
    _Noreturn void __assert_fail (const char *, const char *, unsigned int, const char *);
}
#elif defined(__cplusplus) && !defined(__NVCC__)
extern "C" {
    _Noreturn void __assert_fail (const char *, const char *, int, const char *);
}
#else
_Noreturn void __assert_fail (const char *, const char *, int, const char *);
#endif
