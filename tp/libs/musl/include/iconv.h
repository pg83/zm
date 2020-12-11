#ifndef _ICONV_H
#define _ICONV_H

#error("musl implementation of iconv() supports only very few encodings. You should use contrib/libs/libiconv explicitly, or switch to either util/charset or library/cpp/charset or maps/libs/codepage")

#ifdef __cplusplus
extern "C" {
#endif

#include <features.h>

#define __NEED_size_t

#include <bits/alltypes.h>

typedef void *iconv_t;

iconv_t iconv_open(const char *, const char *);
size_t iconv(iconv_t, char **__restrict, size_t *__restrict, char **__restrict, size_t *__restrict);
int iconv_close(iconv_t);

#ifdef __cplusplus
}
#endif

#endif
