#include <euler/lib/cache.h>

#include <string>
#include <iostream>

static const std::string d1[] = {
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
};

static const std::string d2[] = {
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
};

static const std::string d3[] = {
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
};

int main() {
    auto cvt = cacher1_t<int, std::string>([] (int n, auto& cvt) -> std::string {
        if (n < 10) {
            return d1[n];
        }

        if (n < 20) {
            return d2[n - 10];
        }

        if (n < 100) {
            auto res = d3[n / 10 - 2];
            auto m = n % 10;

            if (m == 0) {
                return res;
            }

            return res + "-" + cvt(m);
        }

        if (n < 1000) {
            auto res = cvt(n / 100) + " hundred";
            auto m = n % 100;

            if (m == 0) {
                return res;
            }

            return res + " and " + cvt(m);
        }

        return "one thousand";
    });

    size_t cnt = 0;

    for (int i = 1; i <= 1000; ++i) {
        std::cout << cvt(i) << std::endl;

        for (auto ch : cvt(i)) {
            if (ch != ' ' && ch != '-') {
                ++cnt;
            }
        }
    }

    std::cout << cnt << std::endl;
}
