
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue order"

//x pre={
// task: define a lambda expression that
// serves as a comparison function
// for sorting by absolute value
//x }

//x step={
auto cmp = [](int l, int r) {
	return std::abs(l) < std::abs(r);
};
//x }

//x post={
std::priority_queue
  <int, std::vector<int>, decltype(cmp)>
  pq(cmp);

// Note: cmp is a function object
// (i.e., it defines operator()).
// If it does NOT capture variables it can be casted
// to a function pointer:
bool (*fp)(int l, int r) = cmp;

pq.push(1);
pq.push(-2);
pq.push(3);
pq.push(-4);

assert((-4==pq.top()));
pq.pop();
assert((3==pq.top()));
//x }

return 0;
}
