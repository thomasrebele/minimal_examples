
#include <cassert>
#include <vector>
#include <string>
#include <stdexcept>
#include <iostream>

int main() {

//x description="vector illegal access"

//x pre={
std::vector<int> v {1,2};

// task: v[10], v.at(10), what happens?
//x }

//x step={
// v[10] is undefined behavior
try {
	v.at(10); // throws an exception
} catch(const std::out_of_range& oor) {
	assert((std::string(oor.what()).find("10") >= 0));
}
//x }

return 0;
}
