
#include <cassert>
#include <unordered_map>
#include <string>

int main() {

//x description="insert on unordered map"

//x pre={
std::unordered_map<std::string, std::string> m;
m.insert({"key", "value1"});
m.insert({"key", "value2"});
// question: what is m["key"]?
//x }

//x step={
assert(("value1" == m["key"]));
// caveat: insert does not update existing entries!
//x }


return 0;
}
