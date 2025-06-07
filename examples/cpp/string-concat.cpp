
#include <string>
#include <iostream>
#include <cassert>

int main() {

//x description="searching in strings"

//x pre={
std::string s = "hello ";
// task: append "foobar" (two ways)
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
