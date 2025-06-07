
#include <string>
#include <iostream>
#include <cassert>

int main() {

//x description="changing strings"

//x pre={
std::string s = "hello!";
// task: modify the string to "hello world!"
//x }

//x step={
s.insert(5, " world");
//x }

//x post={
assert(("hello world!" == s));
//x }

return 0;
}
