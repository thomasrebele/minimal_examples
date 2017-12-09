#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure capturing vector (2)"
//x level=12
/*
//x pre={
let mut a = vec![10];
let f = |x| x+a[0]; 

a[0] = 20;
let b = f(1);
// a? b?
//x }
*/

//x step={
// compile error: cannot borrow `a` as mutable because it is also borrowed as immutable
//x }

}
