
#include <cassert>
#include <deque>
#include <string>

int main() {

//x description="remove elements from deque"

//x pre={
std::deque<int> d {1,2};

// task: remove the last element from the deque
//x }

//x step={
d.pop_back();
// no return value!
//x }

return 0;
}
