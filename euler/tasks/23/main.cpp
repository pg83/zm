#include <euler/lib/primes.h>

#include <unordered_set>
#include <vector>
#include <numeric>
#include <iostream>

template <class T>
bool is_abundand(T t) {
    return proper_divisors_sum(t) > t;
}

int main() {
    std::vector<int> ab;
    std::unordered_set<int> result;

    for (int i = 1; i <= 28123; ++i) {
        if (is_abundand(i)) {
            ab.push_back(i);
        }

        result.insert(i);
    }

    for (auto x : ab) {
        for (auto y : ab) {
            result.erase(x + y);
        }
    }

    std::cout << std::accumulate(result.begin(), result.end(), 0) << std::endl;
}
