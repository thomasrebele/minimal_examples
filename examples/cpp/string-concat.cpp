
#include <string>
#include <iostream>
#include <cassert>

int main() {

//x description="modifying strings"

//x pre={
std::string s = "hello ";
// task: append "foobar" (2 ways)
//x }

//x step={
s += "foo";
// or
s.append("bar");
//x }

//x post={
assert(("hello foobar" == s));
//x }

return 0;
}
