#include <euler/lib/euler.h>

static int gen3(int n) {
    return n * (n + 1) / 2;
}

static int gen4(int n) {
    return n * n;
}

static int gen5(int n) {
    return n * (3 * n - 1) / 2;
}

static int gen6(int n) {
    return n * (2 * n - 1);
}

static int gen7(int n) {
    return n * (5 * n - 3) / 2;
}

static int gen8(int n) {
    return n * (3 * n - 2);
}

int main() {
    using el_t = std::pair<int, int>;
    using path_t = std::vector<el_t>;
    using paths_t = std::vector<path_t>;

    path_t data;

    auto add = [&](auto f, auto n) {
        for (int i = 1; i < 200; ++i) {
            auto r = f(i);

            if (r >= 1000 && r <= 9999) {
                data.emplace_back(r, n);
            }
        }
    };

    add(gen3, 3);
    add(gen4, 4);
    add(gen5, 5);
    add(gen6, 6);
    add(gen7, 7);
    add(gen8, 8);

    std::map<int, path_t> r;

    for (const auto& n : data) {
        r[n.first / 100].push_back(n);
    }

    auto good_path = [](const path_t& p) -> bool {
        std::set<int> res;

        for (const auto& v : p) {
            res.insert(v.second);
        }

        return res.size() == p.size();
    };

    auto calc = memoized([&] (auto& calc, int l, int f, int s) -> paths_t {
        path_t n;

        n.emplace_back(f, s);

        if (l == 0) {
            return {n};
        }

        paths_t res;

        if (auto nbs = r.find(f % 100); nbs != r.end()) {
            for (const auto& nb : nbs->second) {
                for (const auto& p : calc(l - 1, nb.first, nb.second)) {
                    path_t tmp = n;

                    tmp.insert(tmp.end(), p.begin(), p.end());

                    if (good_path(tmp)) {
                        res.push_back(tmp);
                    }
                }
            }
        }

        return res;
    });

    for (const auto& x : data) {
        for (const auto& p : calc(5, x.first, x.second)) {
            if (p.front().first / 100 == p.back().first % 100) {
                std::cout << p << std::endl;

                int res = 0;

                for (const auto& v : p) {
                    res += v.first;
                }

                std::cout << res << std::endl;

                return 0;
            }
        }
    }
}
