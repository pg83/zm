#include <euler/lib/algo.h>
#include <euler/lib/types.h>

#include <string>
#include <iostream>

static std::string keyf(uint n) {
    return sorted(std::to_string(n));
}

int main() {
    for (uint i = 1; ; ++i) {
        auto k = keyf(i);

        if (k == keyf(2 * i)) {
            if (k == keyf(2 * i)) {
                if (k == keyf(3 * i)) {
                    if (k == keyf(4 * i)) {
                        if (k == keyf(5 * i)) {
                            if (k == keyf(6 * i)) {
                                std::cout << i << std::endl;

                                break;
                            }
                        }
                    }
                }
            }
        }
    }
}
