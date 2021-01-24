#include <euler/lib/euler.h>

int main() {
    auto matrix = read_matrix("81_matrix.txt", ',');
    int dim = sqrt_int(matrix.size());

    std::cout << dim << " " << matrix.size() << std::endl;

    auto u = [&](int n) -> std::pair<int, int> {
        return {n % dim, n / dim};
    };

    auto w = [&](int x, int y) -> int {
        return y * dim + x;
    };

    auto nbs = [&](int n) -> std::vector<int> {
        std::vector<int> res;

        if (n == -1) {
            res.push_back(0);

            return res;
        }

        if (n == dim * dim - 1) {
            res.push_back(-2);

            return res;
        }

        auto [x, y] = u(n);

        if (x < dim - 1) {
            res.push_back(w(x + 1, y));
        }

        if (y < dim - 1) {
            res.push_back(w(x, y + 1));
        }

        return res;
    };

    auto weight = [&](int /*fr*/, int to) -> int {
        if (to == -2) {
            return 1;
        }

        return matrix[to];
    };

    dijkstra_t::nodes_t nodes;

    nodes.insert(-2);
    nodes.insert(-1);

    for (int i = 0; i < (int)matrix.size(); ++i) {
        nodes.insert(i);
    }

    dijkstra_t res(-1, nodes, nbs, weight);

    std::cout << res.distance(-2) - 1 << std::endl;
}
