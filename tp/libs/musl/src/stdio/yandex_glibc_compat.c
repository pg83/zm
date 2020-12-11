#include <stdio.h>

FILE *tmpfile64(void) {
    return tmpfile();
}

FILE *fopen64(const char *__restrict x, const char *__restrict y) {
    return fopen(x, y);
}

FILE *freopen64(const char *__restrict x, const char *__restrict y, FILE *__restrict z) {
    return freopen(x, y, z);
}

int fseeko64(FILE * x, off_t y, int z) {
    return fseeko(x, y, z);
}

off_t ftello64(FILE * x) {
    return ftello(x);
}

int fgetpos64(FILE *__restrict x, fpos_t *__restrict y) {
    return fgetpos(x, y);
}

int fsetpos64(FILE * x, const fpos_t * y) {
    return fsetpos(x, y);
}
