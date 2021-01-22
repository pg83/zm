#pragma once

#include <ostream>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

template <class K, class V>
std::ostream& operator<<(std::ostream& o, const std::pair<K, V>& v);

template <class T>
std::ostream& operator<<(std::ostream& o, const std::vector<T>& v);

template <class T>
std::ostream& operator<<(std::ostream& o, const std::deque<T>& v);

template <class K, class V>
std::ostream& operator<<(std::ostream& o, const std::map<K, V>& v);

template <class K, class V>
std::ostream& operator<<(std::ostream& o, const std::unordered_map<K, V>& v);

template <class V>
std::ostream& operator<<(std::ostream& o, const std::set<V>& v);

template <class V>
std::ostream& operator<<(std::ostream& o, const std::unordered_set<V>& v);

template <class I>
void out(std::ostream& o, I b, I e) {
    bool first = true;

    o << "[";

    for (auto x = b; x != e; ++x) {
        if (first) {
            first = false;
        } else {
            o << ", ";
        }

        o << *x;
    }

    o << "]";
}

template <class K, class V>
std::ostream& operator<<(std::ostream& o, const std::pair<K, V>& v) {
    return o << '(' << v.first << ", " << v.second << ')';
}

template <class T>
std::ostream& operator<<(std::ostream& o, const std::vector<T>& v) {
    out(o << 'V', v.begin(), v.end());

    return o;
}

template <class T>
std::ostream& operator<<(std::ostream& o, const std::deque<T>& v) {
    out(o << 'D', v.begin(), v.end());

    return o;
}

template <class K, class V>
std::ostream& operator<<(std::ostream& o, const std::map<K, V>& v) {
    out(o << 'M', v.begin(), v.end());

    return o;
}

template <class K, class V>
std::ostream& operator<<(std::ostream& o, const std::unordered_map<K, V>& v) {
    out(o << "H", v.begin(), v.end());

    return o;
}

template <class V>
std::ostream& operator<<(std::ostream& o, const std::set<V>& v) {
    out(o << 'S', v.begin(), v.end());

    return o;
}

template <class V>
std::ostream& operator<<(std::ostream& o, const std::unordered_set<V>& v) {
    out(o << 'H', v.begin(), v.end());

    return o;
}
