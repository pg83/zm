#include <euler/lib/euler.h>

int main() {
    std::map<char, std::vector<char>> deps;

    for (auto& l : read_lines("./79_keylog.txt")) {
        deps[l[0]].push_back(l[1]);
        deps[l[1]].push_back(l[2]);
    }

    std::set<char> v;
    std::string res;
    std::function<void (char)> visit;

    visit = [&] (char n) {
        for (auto d : deps[n]) {
            visit(d);
        }

        if (v.find(n) == v.end()) {
            v.insert(n);
            res += n;
        }
    };

    visit('7');

    std::cout << reversed(res) << std::endl;
}
