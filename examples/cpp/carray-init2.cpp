
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="C-array"

//x pre={
int a[3] {1};
// task: what is stored in the C-array?
//x }

//x step={
assert((1 == a[0]));
assert((0 == a[1]));
assert((0 == a[2]));
//x }

return 0;
}
