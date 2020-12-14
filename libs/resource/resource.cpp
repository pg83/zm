#include "resource.h"

#include <deque>
#include <string>
#include <unordered_map>
#include <iostream>

using namespace std;

namespace {
    struct res_holder_t {
        void store(string_view path, string_view data) {
            values_.emplace_back(path, data);

            const auto& b = values_.back();

            map_[b.first] = b.second;
        }

        string_view load(string_view path) const {
            auto it = map_.find(path);

            if (it == map_.end()) {
                throw runtime_error("unknown path");
            }

            return it->second;
        }

        string_view key(size_t n) const noexcept {
            return values_[n].first;
        }

        string_view index(size_t n) const noexcept {
            return values_[n].second;
        }

        size_t count() const noexcept {
            return values_.size();
        }

        static res_holder_t& instance() noexcept {
            static res_holder_t rh;

            return rh;
        }

        unordered_map<string_view, string_view> map_;
        deque<pair<string, string>> values_;
    };
}

void resource::store(string_view path, string_view data) {
    res_holder_t::instance().store(path, data);
}

string_view resource::load(string_view path) {
    return res_holder_t::instance().load(path);
}

string_view resource::key(size_t n) noexcept {
    return res_holder_t::instance().key(n);
}

string_view resource::index(size_t n) noexcept {
    return res_holder_t::instance().index(n);
}

size_t resource::count() noexcept {
    return res_holder_t::instance().count();
}
