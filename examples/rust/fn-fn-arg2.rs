#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with function parameter argument (2)"

//x pre={
fn print(n: i32) {
    println!("{}", n);
}

fn twice(f: fn(i32) -> (), arg: i32) {
    f(arg); f(arg);
}

// twice(|x| {println!("{}", x);}, 123); possible ?
//x }

//x step={
// yes, "closure" does not use variables from outside, so it's just a function
//x }

fn main() {
    let a = 123;
}

