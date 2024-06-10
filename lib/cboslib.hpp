// lib/cbos.hpp
#ifndef CBOS_HPP
#define CBOS_HPP

#include <thread>
#include <chrono>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

inline void msleep(int milliseconds) {
    std::this_thread::sleep_for(std::chrono::milliseconds(milliseconds));
}

inline std::string randomcolor() {
    static const std::vector<std::string> color_choices = {
        "\033[31m",  // RED
        "\033[32m",  // GREEN
        "\033[33m",  // YELLOW
        "\033[34m",  // BLUE
        "\033[35m",  // MAGENTA
        "\033[36m",  // CYAN
        "\033[37m",  // WHITE
        "\033[90m",  // LIGHTBLACK_EX
        "\033[94m",  // LIGHTBLUE_EX
        "\033[96m",  // LIGHTCYAN_EX
        "\033[92m",  // LIGHTGREEN_EX
        "\033[95m",  // LIGHTMAGENTA_EX
        "\033[91m",  // LIGHTRED_EX
        "\033[97m",  // LIGHTWHITE_EX
        "\033[93m"   // LIGHTYELLOW_EX
    };
    static bool initialized = false;
    if (!initialized) {
        std::srand(static_cast<unsigned int>(std::time(nullptr)));
        initialized = true;
    }
    int random_index = std::rand() % color_choices.size();
    return color_choices[random_index];
}

inline std::string resetcolor() {
    return "\033[0m";
}

#endif // CBOS_HPP
