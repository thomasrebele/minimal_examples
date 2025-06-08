
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

int result1 = y->Foo::f();
int result2 = z->Foo::f();
// what is result1, what is result2?
//x }

//x step={
// we explictly call Foo's f,
// no resolution happens!
assert((0 == result1));
assert((0 == result2));
//x }

return 0;
}
