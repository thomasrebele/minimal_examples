#[allow(unused_variables)]

//x step={
fn f(slice: &[i32]) {
// ...
}
//x }

fn main() {

//x description="function on array slices"
//x level=5
//x pre={
let _a = [0,1,2,3,4];

f(&_a);
// slice with content [2,3]
f(&_a[2..4]); 
//x }

}
