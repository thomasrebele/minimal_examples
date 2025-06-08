
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

// task: call Bar's f
int result;
//x }

//x step={
result = x.f();
//x }

//x post={
assert((1 == result));
//x }

return 0;
}
