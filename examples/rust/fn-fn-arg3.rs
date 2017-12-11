#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function return type"

//x pre={
fn print(n: i32) {
    println!("{}", n);
}

fn twice(f: fn(i32) -> (), arg: i32) {
    f(arg); f(arg);
}

// let a = 0;
// twice(|x| {println!("{}", a);}, 123); possible ?
//x }

//x step={
// no, compile error; closure captures a, so it cannot be passed as a function pointer
//x }

fn main() {
//    let a = 123;
//    twice(|x| {println!("{}", a);}, 123); 
}

