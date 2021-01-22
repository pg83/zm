#include <euler/lib/euler.h>

bool is_leap(int year) {
    if (year % 4 != 0) {
        return false;
    }

    if (year % 100 == 0) {
        if (year % 400 != 0) {
            return false;
        }
    }

    return true;
}

static const int days[] = {
    31, //jan
    0, //feb
    31, //mar
    30, //apr
    31, //may
    30, //jun
    31, //jul
    31, //aug
    30, //sep
    31, //oct
    30, //nov
    31, //dec
};

template <class F>
void for_each_day(int fr, int to, F&& f) {
    for (int y = fr; y < to; ++y) {
        for (int m = 0; m < 12; ++m) {
            auto dd = days[m];

            if (dd == 0) {
                if (is_leap(dd)) {
                    dd = 29;
                } else {
                    dd = 28;
                }
            }

            for (int d = 0; d < dd; ++d) {
                f(y, d + 1);
            }
        }
    }
}

int main() {
    int wd = 0;
    int res = 0;

    for_each_day(1900, 2001, [&] (int y, int d) {
        if (y > 1900) {
            if (wd == 6) {
                if (d == 1) {
                    ++res;
                }
            }
        }

        wd = (wd + 1) % 7;
    });

    std::cout << res << std::endl;
}
