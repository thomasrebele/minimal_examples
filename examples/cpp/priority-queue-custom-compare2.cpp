
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue order"

//x pre={
// task: define a pq sorting by absolute value
auto cmp = [](int l, int r) {
	return std::abs(l) < std::abs(r);
};
//x }

//x step={
std::priority_queue
  <int, std::vector<int>, decltype(cmp)>
  pq(cmp);
//x }

//x post={
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
