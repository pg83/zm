#pragma once

#include <string>

#include <stddef.h>

namespace io {
    class output_i;

    class input_i {
    public:
        input_i() noexcept;
        virtual ~input_i();

        size_t read(void* data, size_t len) {
            if (len == 0) {
                return 0;
            }

            return do_read(data, len);
        }

        size_t read_exact(void* data, size_t len);
        std::string read_all();
        uint64_t read_all(output_i& out);

    protected:
        virtual size_t do_read(void* data, size_t len) = 0;
    };

    class output_i {
    public:
        output_i() noexcept;
        virtual ~output_i();

        void write(const void* data, size_t len) {
            do_write(data, len);
        }

    protected:
        virtual void do_write(const void* data, size_t len) = 0;
    };

    uint64_t transfer_data(input_i& in, output_i& out);
}
