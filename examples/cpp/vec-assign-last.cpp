
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="vector assignment"

//x pre={
std::vector<int> v {1,2};

// task: change the last element to 5,
// assuming the length of v is unknown
//x }

//x step={
v.back() = 5;
//x }

//x post={
assert((5 == v[1]));
//x }

return 0;
}
