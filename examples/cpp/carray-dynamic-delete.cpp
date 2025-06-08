
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="dynamic C-array"

//x pre={
// task: fix the following program:
int* a = new int[3] {1,2,3};
assert((1 == a[0]));
//x }

//x step={
delete[] a;
// every "new" needs to be paired with a "delete"
// otherwise there would be a memory leak
//x }

return 0;
}
