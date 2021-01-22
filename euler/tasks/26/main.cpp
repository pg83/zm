#include <euler/lib/euler.h>

int reciprocal_cycle(int n, int m) {
    size_t cnt = 0;
    std::map<int, int> pos;

    while (n > 0) {
        if (pos.find(n) == pos.end()) {
            pos[n] = cnt++;
            n = (n % m) * 10;
        } else {
            return cnt - pos[n];
        }
    }

    return 0;
}

int main() {
    int mr = 0;
    int mi = 0;

    for (int i = 1; i <= 1000; ++i) {
        auto r = reciprocal_cycle(1, i);

        if (r > mr) {
            mr = r;
            mi = i;

            std::cout << mi << " " << mr << std::endl;
        }
    }

    std::cout << mi << std::endl;
}
