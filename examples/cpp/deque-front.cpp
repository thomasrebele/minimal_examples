
#include <cassert>
#include <deque>
#include <string>

int main() {

//x description="access elements of deque"

//x pre={
std::deque<int> d {1,2};

// task: access the first element of
// the deque (2 ways)
int el1, el2;
//x }

//x step={
el1 = d.front();
// or
el2 = d[0];
//x }



//x post={
assert((1 == el1));
assert((1 == el2));
//x }
//
return 0;
}
