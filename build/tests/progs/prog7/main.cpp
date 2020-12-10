#include <build/tests/progs/prog7/atoi.h>

#include <string_view>
#include <iostream>
#include <stdexcept>

using namespace std;

template <class T>
static T parse_ragel(const char* b, const char* e) {
    T t = 0;

    if (!parse_stream_unsigned(t, b, e)) {
        return t;
    }

    throw system_error(EINVAL, std::system_category(), "parse_ragel");
}

template <class T>
static T parse_ragel(string_view s) {
    return parse_ragel<T>(s.begin(), s.end());
}

int main(int, char** argv) {
    cout << parse_ragel<unsigned>(string_view(argv[1])) << endl;
}
