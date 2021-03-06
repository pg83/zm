#include <euler/lib/euler.h>

template <class T>
ratio_t<T> left_nearest(ratio_t<T> v, T maxdiv) {
    ratio_t<T> res(2, 5);

    while (res.b < maxdiv) {
        res.a += v.a;
        res.b += v.b;
    }

    while (res.b > maxdiv) {
        res.a -= v.a;
        res.b -= v.b;
    }

    return res;
}

int main() {
    auto res = left_nearest(ratio_t(3, 7), 1000000);

    std::cout << res << " " << res.a << std::endl;
}
