#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure capturing integer (2)"
//x level=11
/*
//x pre={
let mut a = 10;
let f = |x| x+a; 

a = 20;
let b = f(1);
// a? b?
//x }
*/

//x step={
// compile error: cannot assign to `a` because it is borrowed
//x }

}
