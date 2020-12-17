#include <string>

#include <stddef.h>

namespace io {
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

    protected:
        virtual size_t do_read(void* data, size_t len) = 0;
    };
}
