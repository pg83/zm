#include <euler/lib/euler.h>

int main() {
    std::set<int> pows;

    for (size_t i = 0; i <= 100; ++i) {
        pows.insert(i * i);
    }

    size_t res = 0;

    for (size_t i = 2; i <= 10000; ++i) {
        if (pows.find(i) == pows.end()) {
            if (qir_t<size_t>::root_of(i).cont_fraction().size() % 2 == 0) {
                ++res;
            }
        }
    }

    std::cout << res << std::endl;
}
