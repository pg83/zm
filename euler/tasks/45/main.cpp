#include <map>
#include <iostream>

int main() {
    std::map<long int, int> cnt;

    for (long int n = 0; n < 1000000; ++n) {
        ++cnt[(n * (n + 1)) / 2];
        ++cnt[(n * (3 * n - 1)) / 2];
        ++cnt[(n * (2 * n - 1))];
    }

    for (auto it = cnt.begin(); it != cnt.end(); ++it) {
        if (it->second == 3 && it->first > 50000) {
            std::cout << it->first << std::endl;

            break;
        }
    }
}
