
#include <cassert>
#include <vector>
#include <string>
#include <iostream>

//x pre={
class Foo {
public:
	int a = 0;
	int f() {return a;}
};

class Bar : public Foo {
public:
	virtual int f() {return a+1;}
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
// Foo's f is declared non-virtual
assert((0 == result1));

// Bar's f is declared virtual
// so it will be resolved
assert((2 == result2));
//x }

return 0;
}
