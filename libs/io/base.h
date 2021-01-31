#pragma once

#include <libs/platform/types.h>

#include <string>

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

        bool read_char(char& ch) {
            return read(&ch, 1) > 0;
        }

        size_t read_exact(void* data, size_t len);
        std::string read_all();
        ui64 read_all(output_i& out);
        bool read_line(std::string& l);
        size_t read_to(std::string& l, char to);

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

    ui64 transfer_data(input_i& in, output_i& out);
}
