
#include <cassert>
#include <vector>
#include <string>
#include <queue>

int main() {

//x description="priority queue usage"

//x pre={
std::priority_queue<int> pq;

pq.push(2);
pq.push(1);
pq.push(3);

// task: what is the result of pq.top()?
int top = pq.top();
//x }

//x step={
assert((3 == top));
//x }

return 0;
}
