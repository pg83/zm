#include <libs/io/mem.h>

#include <gtest/gtest.h>

using namespace io;

TEST(TestIO, ReadLine) {
    const std::string data = "ab\ncd\r\n\n";
    memory_input_t mi(data.data(), data.size());
    std::string line;

    EXPECT_TRUE(mi.read_line(line));
    EXPECT_EQ(line, "ab");

    EXPECT_TRUE(mi.read_line(line));
    EXPECT_EQ(line, "cd");

    EXPECT_TRUE(mi.read_line(line));
    EXPECT_EQ(line, "");

    EXPECT_FALSE(mi.read_line(line));
}
