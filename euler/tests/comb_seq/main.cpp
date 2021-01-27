#include <euler/lib/euler.h>

int main() {
    {
        for (const auto& c : combination_sequence(0, 10)) {
            std::cout << c << std::endl;
        }
    }

    std::cout << "-------------" << std::endl;

    {
        for (const auto& c : combination_sequence(3, 5)) {
            std::cout << c << std::endl;
        }
    }
}
