
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

// task: call Foo's f
int result;
//x }

//x step={
result = x.Foo::f();
//x }

//x post={
assert((0 == result));
//x }

return 0;
}
