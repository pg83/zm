#include <iostream>

int main() {
    int s = 0;
    int c = 1;
    int i = 2;

    while (true) {
        s += c;
        c += i;

        s += c;
        c += i;

        s += c;
        c += i;

        s += c;
        c += i;

        i += 2;

        if (c == 1001 * 1001) {
            s += c;

            break;
        }
    }

    std:: cout << s << std::endl;
}
