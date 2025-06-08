
#include <cassert>
#include <vector>
#include <string>


//x pre={
class Foo {
public:
	int a;
};
//x }


int main() {

//x description="class member"

//x pre={
Foo* x = new Foo;

// task: set the member a to 1
// (2 ways)
//x }

//x step={
(*x).a = 1;
// or
x->a = 1;
//x }

//x post={
delete x;
//x }

return 0;
}
