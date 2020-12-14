#include "misc.h"

#include <fstream>
#include <exception>

using namespace std;

string io::read_file(const char* fpath) {
    ifstream is(fpath, ios::binary | ios::ate);
    auto size = is.tellg();
    string str(size, '\0');

    is.seekg(0);

    if (is.read(&str[0], size)) {
        return str;
    }

    throw runtime_error("can not read file");
}
