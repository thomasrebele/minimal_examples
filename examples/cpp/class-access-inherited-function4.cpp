
#include <cassert>
#include <vector>
#include <string>
#include <iostream>

//x pre={
class Foo {
public:
	int a = 0;
	virtual int f() {return a;}
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
// Foo's f is virtual, so it is resolved at runtime
// (that means there is a small performance penality
// compared to non-virtual member functions)
assert((1 == result));
//x }

return 0;
}
