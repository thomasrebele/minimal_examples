
#include <cassert>
#include <deque>
#include <string>

int main() {

//x description="remove elements from deque"

//x pre={
std::deque<int> d {1,2};

// task: remove the first element from the deque
//x }

//x step={
d.pop_front();
// no return value!
//x }

return 0;
}
