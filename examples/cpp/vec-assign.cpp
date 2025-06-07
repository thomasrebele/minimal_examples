
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="vector assignment"

//x pre={
std::vector<int> v1 {1,2};
std::vector<int> v2 {7,8};

v1 = v2;
v2[0] = 10;

// task: what is the content of v1 and v2?
//x }

//x step={
assert((std::vector<int>{7,8} == v1));
// v1 is a copy, so it is
// not affected by the change of v2
assert((std::vector<int>{10,8} == v2));
//x }

return 0;
}
