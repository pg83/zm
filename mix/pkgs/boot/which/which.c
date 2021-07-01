#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv) {
    char buf[1000000];
    char* token;
    char* string;

    if (argc < 2) {
        return 0;
    }

    string = strdup(getenv("PATH"));

    while ((token = strsep(&string, ":")) != NULL) {
        sprintf(buf, "%s/%s", token, argv[1]);

        if (fopen(buf, "r")) {
            printf("%s\n", buf);

            return 0;
        }
    }

    return 1;
}
