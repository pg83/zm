#include <set>
#include <iostream>

int main() {
    std::set<int> tr;
    std::set<int> res;

    for (int i = 1; i <= 10000; ++i) {
        tr.insert((i * (3 * i - 1)) / 2);
    }

    for (auto i : tr) {
        for (auto j : tr) {
            if (i > j) {
                auto p1 = i + j;
                auto p2 = i - j;

                if (tr.find(p1) != tr.end()) {
                    if (tr.find(p2) != tr.end()) {
                        res.insert(p2);
                    }
                }
            }
        }
    }

    std::cout << *res.begin() << std::endl;
}
