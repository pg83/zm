#include <string.h>

#undef strcpy

char *strcpy(char *restrict d, const char *restrict s)
{
    char* r;

    r = d;

    for (; (*d=*s); s++, d++);

    return r;
}
