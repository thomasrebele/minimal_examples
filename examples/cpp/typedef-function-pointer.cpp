
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue order"

//x pre={
auto cmp = [](int l, int r) { return l < r; };
// task: rewrite the following using a type definition
bool (*fp1)(int l, int r) = cmp;
//x }

//x step={
typedef bool (*FP)(int l, int r);
FP fp2 = cmp;
//x }

//x post={
assert((fp1(1,2) == fp2(1,2)));
assert((fp1(2,1) == fp2(2,1)));
//x }

return 0;
}
