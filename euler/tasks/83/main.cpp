#include <euler/lib/euler.h>

int main() {
    auto matrix = read_matrix("p083_matrix.txt", ',');
    auto dim = (int)sqrt_int(matrix.size());

    auto u = [&](int n) -> std::pair<int, int> {
        return {n % dim, n / dim};
    };

    auto w = [&](int x, int y) -> int {
        return y * dim + x;
    };

    auto links = [&](int n) -> std::vector<int> {
        if (n == -1) {
            return {0};
        }

        if (n == dim * dim - 1) {
            return {-2};
        }

        auto [x, y] = u(n);

        std::vector<int> res;

        if (x > 0) {
            res.push_back(w(x - 1, y));
        }

        if (x < dim - 1) {
            res.push_back(w(x + 1, y));
        }

        if (y > 0) {
            res.push_back(w(x, y - 1));
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

    std::vector<int> nodes{-1, -2};

    for (int i = 0; i < (int)matrix.size(); ++i) {
        nodes.push_back(i);
    }

    std::cout << dijkstra_distance(-1, -2, nodes, links, weight) - 1 << std::endl;
}
