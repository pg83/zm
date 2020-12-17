#include "misc.h"
#include "file.h"

std::string io::read_file(const char* fpath) {
    return file_input_t(fpath).read_all();
}

std::string io::read_file(const std::string& path) {
    return read_file(path.c_str());
}
