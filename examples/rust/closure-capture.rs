#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure capturing integer"
//x pre={
let a = 10;
let f = |x| x+a; 

let b = f(1);
// a? b?
//x }
//x step={
// a=10, b=11
//x }

    println!("{}", b);
}
