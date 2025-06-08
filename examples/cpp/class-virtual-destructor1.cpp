
#include <cassert>
#include <vector>
#include <string>


//x pre={
class Foo {
};

class Bar : public Foo {
public:
	int* q;
	Bar() {q = new int[10];}
	~Bar() {delete q;}
};
//x }


int main() {

//x description="class destruction"

//x pre={
Foo* p = new Bar;
delete p;

// task: fix the error!
//x }

//x step={
class Foo {
public:
	// Foo needs a virtual destructor
	// so that the child classes' destructors
	// are called; otherwise the array q
	// would not be freed
	virtual ~Foo() {}
};
//x }

return 0;
}
