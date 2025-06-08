
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

class Baz : public Bar {
public:
	int f() {return a+2;}
};
//x }


int main() {

//x description="class member"

//x pre={
Baz x;
Foo* y = &x;
Bar* z = &x;

int result1 = y->f();
int result2 = z->f();
// what is result1, what is result2?
//x }

//x step={
// f is declared virtual, so it is resolved
assert((2 == result1));

// overridden virtual member functions
// are automatically virtual
assert((2 == result2));
//x }

return 0;
}
