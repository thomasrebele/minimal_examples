
#include <string>
#include <iostream>
#include <cassert>

int main() {

//x description="searching in strings"

//x pre={
std::string s = "hello";
// task: how to get the position of first a substring, e.g., "el"
//x }

//x step={
size_t pos = s.find("el");
assert((pos == 1));
//x }

return 0;
}
