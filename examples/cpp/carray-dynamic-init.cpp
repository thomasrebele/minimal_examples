
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="dynamic C-array"

//x pre={
// task: create a C-array on the heap
// with values 1,2,3
//x }

//x step={
int* a = new int[3] {1,2,3};
//x }

//x post={
assert((1 == a[0]));
delete[] a;
//x }

return 0;
}
