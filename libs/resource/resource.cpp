#include "resource.h"

#include <deque>
#include <string>
#include <unordered_map>

namespace {
    struct res_holder_t {
        void store(std::string_view path, std::string_view data) {
            values_.emplace_back(path, data);

            const auto& b = values_.back();

            map_[b.first] = b.second;
        }

        std::string_view load(std::string_view path) {
            auto it = map_.find(path);

            if (it == map_.end()) {
                throw std::runtime_error("unknown path");
            }

            return it->second;
        }

        std::string_view index(size_t n) const noexcept {
            return values_[n].second;
        }

        size_t count() const noexcept {
            return values_.size();
        }

        static res_holder_t& instance() noexcept {
            static res_holder_t rh;

            return rh;
        }

        std::unordered_map<std::string_view, std::string_view> map_;
        std::deque<std::pair<std::string, std::string>> values_;
    };
}

void resource::store(std::string_view path, std::string_view data) {
    res_holder_t::instance().store(path, data);
}

std::string_view resource::load(std::string_view path) {
    return res_holder_t::instance().load(path);
}

std::string_view resource::index(size_t n) noexcept {
    return res_holder_t::instance().index(n);
}

size_t resource::count() noexcept {
    return res_holder_t::instance().count();
}
