#include <string>
#include <iostream>

template <class T>
bool is_palindromic(T t) {
    auto s = std::to_string(t);

    size_t i = 0;
    size_t j = s.length() - 1;

    while (i < j) {
        if (s[i] != s[j]) {
            return false;
        }

        ++i;
        --j;
    }

    return true;
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
