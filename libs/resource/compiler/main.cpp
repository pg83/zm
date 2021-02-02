#include <libs/io/misc.h>
#include <libs/resource/resource.h>

#include <string>
#include <iostream>

template <class T>
static void gen_header(T& o) {
    o << "namespace resource {\n";
    o << "    void store(const void* key_data, int key_size, const void* value_data, int value_size);\n";
    o << "}\n\n";
    o << "namespace {\n";
    o << "    struct reg_t {\n";
    o << "        reg_t() {\n";
}

template <class T>
static void gen_footer(T& o) {
    o << "        }\n";
    o << "    } REG;\n";
    o << "}\n";
}

template <class T>
static void gen_one(const char* fpath, const char* key, T& o) {
    o << "            {\n";
    o << "                static const unsigned char data[] = {\n";

    size_t cnt = 0;

    for (auto ch : io::read_file(fpath)) {
        ++cnt;

        if (cnt > 16) {
            o << "\n";
            cnt = 0;
        }

        o << (unsigned short)(unsigned char)(ch) << ", ";
    }

    o << "\n";
    o << "                };\n\n";
    o << "                static const char key[] = \"" << key << "\";\n\n";
    o << "                resource::store(key, sizeof(key) - 1, data, sizeof(data));\n";
    o << "            }\n";
}

int main(int argc, char** argv) {
    auto& o = std::cout;

    gen_header(o);

    for (int i = 1; i < argc; i += 2) {
        gen_one(argv[i], argv[i + 1], o);
    }

    gen_footer(o);
}
