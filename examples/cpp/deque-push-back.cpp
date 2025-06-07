
#include <cassert>
#include <deque>
#include <string>

int main() {

//x description="add elements to deque"

//x pre={
std::deque<int> d {1,2};

// task: add 5 as the last element to the deque
//x }

//x step={
d.push_back(5);
//x }

//x post={
assert((5 == d[2]));
//x }

return 0;
}
