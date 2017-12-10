#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="get element from vector (3)"
//x pre={
let a = vec![0,1,2,3];

let b = &a[10]; // what happens?
let c = a.get(10); // what happens?
//x }

//x step={
let b = &a[10]; // panic, program stops
let c = a.get(10); // c is None
//x }

}
