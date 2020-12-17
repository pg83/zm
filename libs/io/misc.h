#pragma once

#include <string>

namespace io {
    std::string read_file(const char* path);
    std::string read_file(const std::string& path);
}
