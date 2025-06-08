
#include <cassert>
#include <vector>
#include <string>


//x pre={
std::vector<std::string> v;

class Foo {
public:
	virtual ~Foo() {v.push_back("~Foo");}
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
assert((2 == v.size()));
assert(("~Bar" == v[0]));
assert(("~Foo" == v[1]));
//x }

return 0;
}
