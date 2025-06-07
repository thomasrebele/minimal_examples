
#include <cassert>
#include <unordered_map>
#include <string>

int main() {

//x description="iteration on unordered map"

//x pre={
std::unordered_map<std::string, std::string> m;
m["key"] = "value";

// task: iterate over the entries
//x }

//x step={
for (const auto& node: m) {
//x }

//x post={
	assert(("key" == node.first));
	assert(("value" == node.second));
}
//x }

return 0;
}
