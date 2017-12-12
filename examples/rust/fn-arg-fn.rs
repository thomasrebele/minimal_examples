#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with function parameter (1)"

//x pre={
fn print(n: i32) {
    println!("{}", n);
}

// fn twice(f: ..., arg: i32) {
//  f(arg); f(arg);
// }
//x }

//x step={
fn twice(f: fn(i32) -> (), arg: i32) {
    f(arg); f(arg);
}
//x }


//x explanation="parameter f is a function pointer; better use Fn, FnMut or FnOnce"

fn main() {

//x post={
twice(print, 0);
//x }
    //let a = 123;
    //twice(|x:i32| {println!("{}", a + x);}, 123);
}

