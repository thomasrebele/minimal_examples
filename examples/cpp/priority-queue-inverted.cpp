
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue order"

//x pre={

std::priority_queue<int> pq_ex;

pq_ex.push(2);
pq_ex.push(1);
pq_ex.push(3);

// task: the above PQ sorts the values as 1,2,3.
// Declare a PQ that sorts the values as 3,2,1.
//x }

//x step={
std::priority_queue
	<int, std::vector<int>, std::greater<int>>
	pq;
//x }

//x post={
pq.push(2);
pq.push(1);
pq.push(3);

assert((3==pq_ex.top()));
assert((1==pq.top()));
//x }


// a test

return 0;
}
