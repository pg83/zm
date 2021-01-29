#pragma once

#if defined(__cplusplus)
extern "C" {
#endif
    int resource_count();

    const char* resource_key_data(int n);
    int resource_key_size(int n);

    const char* resource_value_data(int n);
    int resource_value_size(int n);
#if defined(__cplusplus)
}
#endif
