#include <iostream>
#include <string>
#include <algorithm>
#include "lib/cboslib.hpp"

using namespace std;

int main() {
    ccout("Booting cbos the crappy os\n");
    msleep(500);
    ccout("Loading libraries and variables\n");
    float version = 1.00;
    msleep(300);
    ccout("Done!\n");
    msleep(200);
    ccout("Welcome to C-Bos v1.0.0!\n");
    msleep(200);
    ccout("Type help for a list of commands!\n");

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
            msleep(500);
            return 0;
        }

        else if (lowercmd == "help") {
            cout << "1: Run test (it was in the original so I put it here idk)\n";
            msleep(100);
            cout << "2: Exit (Exits the program wowie)\n";
        }



        else {
            cout << cmd + " is stupid! please try again!\n";
        }
    }
}
