#include <libs/io/misc.h>
#include <libs/xxhash/xxhash.h>
#include <libs/resource/resource.h>

#include <string>
#include <iostream>

template <class T>
static void gen_one(const char* fpath, const char* key, T& out) {
    out << "#include <libs/resource/resource.h>\n\n";

    const auto name = "data_" + std::to_string(xx::hash64(key, 0));

    out << "namespace {\nstatic const unsigned char " << name << "[] = {\n";

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

    out << "\n};\n\nstatic const resource::reg_helper_t register_" << name
        << "(\"" << key << "\", std::string_view((const char*)"
        << name << ", sizeof(" << name << ")" << "));\n}\n";
}

int main(int argc, char** argv) {
    for (int i = 1; i < argc; i += 2) {
        gen_one(argv[i], argv[i + 1], std::cout);
    }
}
