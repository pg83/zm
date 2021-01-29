#include "wrapper.h"

#include <libs/resource/resource.h>

extern "C" {
    int resource_count() {
        return resource::count();
    }

    const char* resource_key_data(int n) {
        return resource::key(n).data();
    }

    int resource_key_size(int n) {
        return resource::key(n).size();
    }

    const char* resource_value_data(int n) {
        return resource::index(n).data();
    }

    int resource_value_size(int n) {
        return resource::index(n).size();
    }
};
