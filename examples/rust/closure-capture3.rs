#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure capturing integer (3)"
//x pre={
// copy-type
let a = 10;
let f = move |x| x+a; 

let b = f(1);
// a? b?
//x }

//x step={
// a=10, b=11
//x }

    println!("{}, {}", a, b);
}
