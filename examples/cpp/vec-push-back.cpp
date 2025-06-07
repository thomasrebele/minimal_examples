
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="add elements to vector"

//x pre={
std::vector<int> v {0,1,2};

// task: add 3 as last element to the vector
//x }

//x step={
v.push_back(3);
//x }

//x post={
assert((3 == v[3]));
//x }

return 0;
}
