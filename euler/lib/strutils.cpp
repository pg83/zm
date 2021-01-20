#include "strutils.h"

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
