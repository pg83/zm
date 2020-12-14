#include <libs/resource/resource.h>

#include <iostream>

using namespace std;

int main() {
    for (size_t n = 0; n < resource::count(); ++n) {
        cout << resource::key(n) << " " << resource::index(n);
    }
}
