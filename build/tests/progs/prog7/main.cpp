#include <build/tests/progs/prog7/atoi.h>

#include <string_view>
#include <iostream>
#include <stdexcept>

using namespace std;

template <class T>
static T ParseRagel(const char* b, const char* e) {
    T t = 0;

    if (!ParseStreamUnsigned(t, b, e)) {
        return t;
    }

    throw runtime_error("shit happen");
}

template <class T>
static T ParseRagel(string_view s) {
    return ParseRagel<T>(s.begin(), s.end());
}

int main() {
    cout << ParseRagel<unsigned>(string_view("123")) << endl;
}
