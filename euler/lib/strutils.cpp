#include "strutils.h"

#include <libs/io/file.h>

size_t digit_sum(const std::string& s) noexcept {
    size_t res = 0;

    for (auto ch : s) {
        res += ch - '0';
    }

    return res;
}

std::vector<std::string> split_string(const std::string& s, char delim) {
	std::vector<std::string> res;
	std::string tmp;

	for (auto ch : s) {
        if (ch == delim) {
            res.push_back(tmp);
            tmp.clear();
        } else {
            tmp += ch;
        }
	}

	if (!tmp.empty()) {
        res.push_back(tmp);
    }

    return res;
}

std::vector<std::string> read_lines(const std::string& path) {
    std::vector<std::string> res;
    io::file_input_t fi(path);
    std::string line;

    while (fi.read_line(line)) {
        res.push_back(line);
    }

    return res;
}

std::vector<int> read_matrix(const std::string& path, char delim) {
    std::vector<int> res;

    for (const auto& l : read_lines(path)) {
        for (auto el : parse_string<int>(l, delim)) {
            res.push_back(el);
        }
    }

    return res;
}
