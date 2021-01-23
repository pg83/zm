#include <euler/lib/euler.h>

static bool is_prime(const std::string& s) {
    return is_prime_stupid(from_string<int>(s));
}

template <class S, class K>
static bool has(const S& s, const K& k) {
    return s.find(k) != s.end();
}

template <class S>
S inter(const S& l, const S& r) {
    if (l.size() > r.size()) {
        return inter(r, l);
    }

    S res;

    for (auto v : l) {
        if (has(r, v)) {
            res.insert(v);
        }
    }

    return res;
}

int main() {
    std::vector<int> primes;

    for (int i = 0; i < 10000; ++i) {
        if (is_prime_stupid(i)) {
            primes.push_back(i);
        }
    }

    std::map<int, std::set<int>> rrr;

    for (auto a : primes) {
        for (auto b : primes) {
            auto sa = std::to_string(a);
            auto sb = std::to_string(b);

            if (is_prime(sa + sb) && is_prime(sb + sa)) {
                rrr[a].insert(b);
                rrr[b].insert(a);
            }
        }
    }

    for (auto [k, items] : rrr) {
        if (items.size() > 3) {
            for (auto& i : items) {
                if (has(rrr, i)) {
                    auto iss = inter(rrr[i], items);

                    if (iss.size() > 2) {
                        for (auto& j : iss) {
                            if (has(rrr, j)) {
                                auto iss2 = inter(rrr[j], iss);

                                if (iss2.size() > 1) {
                                    for (auto& h : iss2) {
                                        if (has(rrr, h)) {
                                            auto iss3 = inter(rrr[h], iss2);

                                            if (iss3.size() > 0) {
                                                std::cout << k + i + j + h + *iss3.begin() << std::endl;

                                                return 0;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
