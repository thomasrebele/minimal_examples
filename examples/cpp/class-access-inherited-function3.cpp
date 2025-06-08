
#include <cassert>
#include <vector>
#include <string>


//x pre={
class Foo {
public:
	int a = 0;
	int f() {return a;}
};

class Bar : public Foo {
public:
	int f() {return a+1;}
};
//x }


int main() {

//x description="class member"

//x pre={
Bar x;
Foo* y = &x;

int result = y->f();
// what is the result?
//x }

//x step={
// *y is of type Foo, so Foo's f is called
assert((0 == result));
//x }

return 0;
}
