#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure capturing vector (3)"
//x level=12
//x pre={
let a = vec![10];
let f = move |x| x+a[0]; 

let b = f(1);
// a? b?
//x }

//x step={
// a is unavailable, b=11
//x }

    println!("{}", b);
}
