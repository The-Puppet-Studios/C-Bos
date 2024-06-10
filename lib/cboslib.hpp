// lib/cbos.hpp
#ifndef CBOS_HPP
#define CBOS_HPP

#include <thread>
#include <chrono>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

inline void msleep(int milliseconds) {
    this_thread::sleep_for(chrono::milliseconds(milliseconds));
}

inline string randomcolor() {
    static const vector<string> color_choices = {
        "\033[31m",  // RED
        "\033[32m",  // GREEN
        "\033[33m",  // YELLOW
        "\033[34m",  // BLUE
        "\033[35m",  // MAGENTA
        "\033[36m",  // CYAN
        "\033[94m",  // LIGHTBLUE_EX
        "\033[96m",  // LIGHTCYAN_EX
        "\033[92m",  // LIGHTGREEN_EX
        "\033[95m",  // LIGHTMAGENTA_EX
        "\033[91m",  // LIGHTRED_EX
        "\033[93m"   // LIGHTYELLOW_EX
    };
    static bool initialized = false;
    if (!initialized) {
        srand(static_cast<unsigned int>(time(nullptr)));
        initialized = true;
    }
    int random_index = rand() % color_choices.size();
    return color_choices[random_index];
}

inline string resetcolor() {
    return "\033[0m";
}

inline void ccout(string strung) {
    cout << randomcolor() << strung << resetcolor();
}

#endif // CBOS_HPP
