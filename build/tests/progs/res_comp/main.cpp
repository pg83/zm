#include <libs/resource/resource.h>

#include <iostream>

int main() {
    {
        static const char data[] = "data1";

        resource::store("/key1", data);
    }

    {
        static const char data[] = "data2";

        resource::store("/key2", data);
    }

    std::cout << resource::load("/key2") << std::endl;
}
