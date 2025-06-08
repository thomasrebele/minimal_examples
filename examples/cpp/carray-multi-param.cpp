
#include <cassert>
#include <vector>
#include <string>

//x step={
void p(int a[][3]) {
	a[1][1] = 123;
}
//x }


int main() {

//x description="C-array"

//x pre={
int a[2][3] = {{0,1,2},{3,4,5}};

// task: define a function that
// makes the assert pass
//x }

//x post={
p(a);
assert((123 == a[1][1]));
//x }

return 0;
}
