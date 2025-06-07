
#include <cassert>
#include <vector>
#include <string>

int main() {

//x description="vector preallocation"

//x pre={
std::vector<int> v;

int n = 10000;
// task: preallocate enough space in the vector for n elements
//x }

n = 10;

//x step={
v.reserve(n);
// caveat: does NOT reduce the capacity if n < v.capacity()
//x }

//x post={
assert((0==v.size()));
assert((n==v.capacity()));
for(int i=0; i<n; i++) {
	v[i] = i*i;
}
//x }

return 0;
}
