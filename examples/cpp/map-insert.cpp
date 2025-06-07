
#include <cassert>
#include <unordered_map>
#include <string>

int main() {

//x description="add entries to unordered map"

//x pre={
std::unordered_map<std::string, std::string> m;
// task: map "key" to "value" (2 ways)
//x }

//x step={
m["key"] = "value";
// or
m.insert_or_assign("key", "value");
// returns a pair (iterator, was_inserted)
//x }

//x post={
assert((1 == m.size()));
//x }
assert(("value" == m["key"]));

return 0;
}
