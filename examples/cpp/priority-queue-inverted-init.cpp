
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue order"

//x pre={
std::priority_queue<int, std::vector<int>, std::greater<int>> pq_ex;

std::vector<int> v{1,2,3,4,5};
for (int i: v) {
	pq_ex.push(i);
}

// task: the above takes O(n log(n)) time,
// how to do it in O(n) time complexity?
//x }

//x step={
std::priority_queue<int, std::vector<int>, std::greater<int>> pq(std::greater<int>(), v);
//x }

//x post={
assert((1==pq_ex.top()));
assert((1==pq.top()));
//x }


// a test

return 0;
}
