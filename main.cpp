#include <iostream>
#include <string>
#include <algorithm>
#include "lib/cboslib.hpp"  // Include the cboslib library

using namespace std;

int main() {
    cout << randomcolor() << "Booting cbos the crappy os" << resetcolor() << endl;
    msleep(500);
    cout << randomcolor() << "Loading libraries" << resetcolor() << endl;
    msleep(300);
    cout << randomcolor() << "Done!" << resetcolor() << endl;
    cout << randomcolor() << "Welcome to C-Bos!" << resetcolor() << endl;

    bool cmdloop = true;
    while (cmdloop) {
        string cmd;
        cout << "\033[33m> \033[0m";  // Yellow color for the prompt
        getline(cin, cmd);
        string lowercmd = cmd;
        transform(lowercmd.begin(), lowercmd.end(), lowercmd.begin(), ::tolower);
        
        if (lowercmd == "run test") {
            cout << "It is working!" << endl;
        }
        
        else if (lowercmd == "shut down" || lowercmd == "exit") {
            cout << "Shutting Down..." << endl;
            msleep(2000);
            return 0;
        }

        else if (lowercmd == "help") {
            cout << "1: Run test (it was in the original so I put it here idk)\n";
            msleep(100);
            cout << "2: Exit (Exits the program wowie)\n";
        }
    }
}
