
#include <cassert>
#include <deque>
#include <string>

int main() {

//x description="access elements of deque"

//x pre={
std::deque<int> d {1,2};

// task: access the last element of the deque (without knowing its size)
int el;
//x }

//x step={
el = d.back();
//x }



//x post={
assert((2 == el));
//x }
//
return 0;
}
