
#include <cassert>
#include <unordered_map>
#include <string>

int main() {

//x description="iteration on unordered map"

//x pre={
std::unordered_map<std::string, std::string> m;
m["key"] = "value";

// task: access the key / value
for (const auto& node: m) {
	std::string key, value;
//x }

//x step={
	key = node.first;
	value = node.second;
//x }

//x post={
	assert(("key" == key));
	assert(("value" == value));
}
//x }

return 0;
}
