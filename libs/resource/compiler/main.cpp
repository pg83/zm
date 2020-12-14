#include <libs/io/misc.h>
#include <libs/xxhash/xxhash.h>
#include <libs/resource/resource.h>

#include <string>
#include <iostream>

using namespace std;

template <class T>
static void gen_one(const char* fpath, const char* key, T& out) {
    out << "#include <libs/resource/resource.h>\n\n";

    const std::string name = "data_" + to_string(xxhash::hash64(key, 0));

    out << "static const unsigned char " << name << "[] = {\n";

    const auto data = io::read_file(fpath);

    auto b = (const unsigned char*)data.begin();
    auto e = b + data.size();

    size_t cnt = 0;

    while (b < e) {
        ++cnt;

        if (cnt > 16) {
            out << "\n";
            cnt = 0;
        }

        out << (unsigned short)(*b) << ", ";

        ++b;
    }

    out << "\n};\n\nnamespace {\n    static const resource::reg_helper_t register_" << name << "(\"" << key << "\", std::string_view((const char*)"
        << name << ", sizeof(" << name << ")" << "));\n}\n";
}

int main(int argc, char** argv) {
    for (size_t i = 1; i < argc; i += 2) {
        gen_one(argv[i], argv[1 + 1], cout);
    }
}
