#include <libs/io/file.h>

#include <iostream>

using namespace io;
using namespace std;

int main(int, char** argv) {
    cout << file_input_t(argv[1]).read_all() << endl;
}
