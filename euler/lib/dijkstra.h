#pragma once

#include "algo.h"

#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <limits>

struct dijkstra_t {
    using nodes_t = std::unordered_set<int>;

    std::unordered_map<int, int> prev;
    std::unordered_map<int, int> dist;

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

    auto path(int dest) const {
        std::vector<int> r;

        r.push_back(dest);

        auto c = dest;

        for (auto p = prev.find(c); p != prev.end(); p = prev.find(c)) {
            c = p->second;
            r.push_back(c);
        }

        return reversed(r);
    }
};

template <class N, class L, class W>
int dijkstra_distance(int fr, int to, N&& nodes, L&& links, W&& weight) {
    return dijkstra_t(fr, dijkstra_t::nodes_t(nodes.begin(), nodes.end()), links, weight).distance(to);
}
