#include <euler/lib/euler.h>

template <class T>
bool is_palindromic(T t) {
    return is_palindrom(std::to_string(t));
}

int main() {
    unsigned max = 0;

    for (unsigned i = 100; i < 999; ++i) {
        for (unsigned j = 100; j < 999; ++j) {
            auto v = i * j;

            if (v > max && is_palindromic(v)) {
                max = v;
            }
        }
    }

    std::cout << max << std::endl;
}
