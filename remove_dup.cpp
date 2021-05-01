//
// Created by rigoligo on 2021/5/2.
//

#include <unordered_set>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
    ifstream in(argv[1]);
    std::unordered_set<std::string> remove_dup;
    std::string buf;

    while(in.good())
    {
        std::getline(in, buf);
        remove_dup.insert(buf);
    }

    ofstream out("去重");
    for(auto &i : remove_dup)
    {
        out << i << std::endl;
    }

    return 0;
}