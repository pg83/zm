#pragma once

#include "algo.h"

#include <set>
#include <map>
#include <vector>
#include <limits>

struct dijkstra_t {
    using nodes_t = std::set<int>;
    using path_t = std::vector<int>;

    std::map<int, int> prev;
    std::map<int, int> dist;

    template <class L, class W>
    dijkstra_t(int source, nodes_t q, L&& nbs, W&& weight) {
        for (auto v : q) {
            dist[v] = std::numeric_limits<int>::max() / 2;
        }

        dist[source] = 0;

        auto min_dist_node = [&]() -> int {
            auto mindist = std::numeric_limits<int>::max();
            auto res = 0;

            for (auto v: q) {
                auto vd = dist[v];

                if (vd < mindist) {
                    res = v;
                    mindist = vd;
                }
            }

            return res;
        };

        while (!q.empty()) {
            auto u = min_dist_node();

            q.erase(u);

            for (auto v : nbs(u)) {
                if (q.find(v) != q.end()) {
                    auto alt = dist[u] + weight(u, v);

                    if (alt < dist[v]) {
                        dist[v] = alt;
                        prev[v] = u;
                    }
                }
            }
        }
    }

    int distance(int dest) {
        return dist[dest];
    }

    path_t path(int dest) const {
        path_t r;

        r.push_back(dest);

        auto c = dest;

        for (auto p = prev.find(c); p != prev.end(); p = prev.find(c)) {
            c = p->second;
            r.push_back(c);
        }

        return reversed(r);
    }
};
