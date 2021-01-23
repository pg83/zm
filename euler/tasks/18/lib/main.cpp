#include "main.h"

#include <euler/lib/euler.h>

namespace {
    using idd_t = int;
    using value_t = int;
    using path_t = std::vector<idd_t>;
    using links_t = std::vector<idd_t>;

    struct graph_t {
        std::vector<value_t> values;
        std::unordered_map<idd_t, links_t> links;

        void dump() const {
            for (auto i : links) {
                for (auto j : i.second) {
                    std::cout << values[i.first] << " -> " << values[j] << std::endl;
                }
            }
        }

        idd_t add_value(value_t v) {
            values.push_back(v);

            return values.size() - 1;
        }

        void add_link(idd_t fr, idd_t to) {
            links[fr].push_back(to);
        }

        const links_t& find_links(idd_t fr) const noexcept {
            auto it = links.find(fr);

            if (it == links.end()) {
                static links_t empty;

                return empty;
            }

            return it->second;
        }

        value_t path_weight(const path_t& p) const noexcept {
            value_t res = 0;

            for (auto& id : p) {
                res += values[id];
            }

            return res;
        }

        path_t calc_max_path(idd_t fr) const {
            static const path_t empty;

            auto calc = memoized([this] (auto& calc, idd_t fr) -> path_t {
                auto& links = find_links(fr);

                value_t maxw = 0;
                auto path_maxw = &empty;

                for (auto id : links) {
                    auto path = &calc(id);
                    auto pathw = path_weight(*path);

                    if (pathw > maxw) {
                        maxw = pathw;
                        path_maxw = path;
                    }
                }

                path_t ret;

                ret.push_back(fr);
                ret.insert(ret.end(), path_maxw->begin(), path_maxw->end());

                return ret;
            });

            return calc(fr);
        }
    };
}

void run_main(const char* path) {
    size_t cnt = 0;
    idd_t lid = 0;
    graph_t gr;

    for (const auto& line : read_lines(path)) {
        for (const auto& f : parse_string<value_t>(line, ' ')) {
            lid = gr.add_value(f);
        }

        std::cout << line << std::endl;

        if (cnt > 0) {
            const idd_t b = lid - 2 * cnt;
            const idd_t e = b + cnt;

            for (idd_t id = b; id < e; ++id) {
                gr.add_link(id, id + cnt);
                gr.add_link(id, id + cnt + 1);
            }
        }

        ++cnt;
    }

    gr.dump();

    auto res = gr.calc_max_path(0);

    for (auto id : res) {
        std::cout << gr.values[id] << std::endl;
    }

    std::cout << gr.path_weight(res) << std::endl;
}
