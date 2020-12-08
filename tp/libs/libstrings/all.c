#include <string.h>

#undef memcpy
#undef strcat
#undef strlen
#undef memset
#undef strcpy
#undef memchr
#undef memmove
#undef memcmp

void *memcpy(void *restrict dest, const void *restrict src, size_t n)
{
	unsigned char *d = dest;
	const unsigned char *s = src;

	for (; n; n--) *d++ = *s++;
	return dest;
}

#define __stpcpy ___stpcpy
#define weak_alias(a, b)

#include <tp/libs/libmusl/src/string/stpcpy.c>
#include <tp/libs/libmusl/src/string/strcat.c>
#include <tp/libs/libmusl/src/string/strlen.c>
#include <tp/libs/libmusl/src/string/memset.c>
#include <tp/libs/libmusl/src/string/strcpy.c>
#include <tp/libs/libmusl/src/string/memchr.c>
#include <tp/libs/libmusl/src/string/memmove.c>
#include <tp/libs/libmusl/src/string/memcmp.c>
