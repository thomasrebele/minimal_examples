
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue initialization"

//x pre={

std::vector<int> v{1,2,3,4,5};
std::priority_queue<int> pq_ex;
for (int i: v) {
	pq_ex.push(i);
}

// task: the above takes O(n log(n)) time,
// how to do it in O(n) time complexity?
//x }

//x step={
std::priority_queue<int> pq(std::less<int>(), v);
//x }

//x post={
assert((5==pq.size()));
assert((5==pq.top()));
assert((pq_ex.top() == pq.top()));
//x }


// a test

return 0;
}
