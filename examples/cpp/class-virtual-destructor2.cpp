
#include <cassert>
#include <vector>
#include <string>


//x pre={
std::vector<std::string> v;

class Foo {
public:
	~Foo() {v.push_back("~Foo");}
};


class Bar : public Foo {
public:
	~Bar() {v.push_back("~Bar");}
};
//x }


int main() {

//x description="class destruction"

//x pre={
Foo* p = new Bar;
delete p;

// task: what's in the vector "v"?
//x }

//x step={
assert((1 == v.size()));
assert(("~Foo" == v[0]));

// caveat: the destructor is non-virtual
// so Bar's destructor is not called
// potentially causing memory leaks!
//x }

return 0;
}
