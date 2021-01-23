#include <euler/lib/euler.h>

template <class T>
ratio_t<T> left_nearest(ratio_t<T> v, T maxdiv) {
    ratio_t<T> res(0);

    if (res.b < maxdiv) {
        T n = (maxdiv - res.b) / v.b;

        res.a += n * v.a;
        res.b += n * v.b;
    }

    while (res.b > maxdiv) {
        res.a -= v.a;
        res.b -= v.b;
    }

    return res;
}

int main() {
    std::cout << left_nearest(ratio_t(3, 7), 1000000).a << std::endl;
}
