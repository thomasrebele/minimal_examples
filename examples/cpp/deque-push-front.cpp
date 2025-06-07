
#include <cassert>
#include <deque>
#include <string>

int main() {

//x description="add elements to deque"

//x pre={
std::deque<int> d {1,2};

// task: add 5 as the first element to the deque
//x }

//x step={
d.push_front(5);
//x }

//x post={
assert((5 == d[0]));
//x }

return 0;
}
