#include <euler/lib/euler.h>

int main() {
    std::unordered_map<std::string, std::vector<ui64>> res;

    for (ui64 i = 1; i < 100000; ++i) {
        res[sorted(std::to_string(i * i * i))].push_back(i);
    }

    std::set<ui64> all;

    for (auto& it : res) {
        if (it.second.size() == 5) {
            all.insert(*it.second.begin());
        }
    }

    std::cout << pow_int(*all.begin(), 3) << std::endl;
}
