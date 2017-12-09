#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure capturing vector"
//x pre={
let a = vec![10];
let f = |x| x+a[0]; 

let b = f(1);
// a? b?
//x }
//x step={
// a=[10], b=11
//x }

    println!("{:?} {}", a, b);
}
