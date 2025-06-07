
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="count elements in vector"

//x pre={
std::vector<int> v {1,2};

// task: how to get the number of elements in v?
//x }

//x step={
assert((2 == v.size()));
//x }

return 0;
}
