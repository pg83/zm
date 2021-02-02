#include "resource.h"

#include <libs/xxhash/xxhash.h>

#include <deque>
#include <unordered_map>
#include <iostream>

namespace {
    struct res_holder_t {
        void store(std::string_view path, std::string_view data) {
            values_.emplace_back(path, data);

            const auto& b = values_.back();

            map_[b.first] = b.second;
        }

        std::string_view load(std::string_view path) const {
            auto it = map_.find(path);

            if (it == map_.end()) {
                throw std::runtime_error("unknown path");
            }

            return it->second;
        }

        std::string_view key(size_t n) const noexcept {
            return values_[n].first;
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

        std::unordered_map<std::string_view, std::string_view, xx::hash_t> map_;
        std::deque<std::pair<std::string_view, std::string_view>> values_;
    };
}

void resource::store(const void* key_data, int key_size, const void* value_data, int value_size) {
    store(std::string_view((const char*)key_data, key_size), std::string_view((const char*)value_data, value_size));
}

void resource::store(std::string_view path, std::string_view data) {
    res_holder_t::instance().store(path, data);
}

std::string_view resource::load(std::string_view path) {
    return res_holder_t::instance().load(path);
}

std::string_view resource::key(size_t n) noexcept {
    return res_holder_t::instance().key(n);
}

std::string_view resource::index(size_t n) noexcept {
    return res_holder_t::instance().index(n);
}

size_t resource::count() noexcept {
    return res_holder_t::instance().count();
}
