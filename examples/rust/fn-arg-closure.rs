#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with closure parameter"

fn main() {

//x pre={
let closure = || println!("hello");

fn twice<F>(f: F)
where F: Fn() -> () {
    f(); f();
}

twice(closure);

// why do we need generics to pass a closure to a function?
//x }

//x step={
// compiler creates an anonymous type for the closure, which is not available to the programmer
//x }

}

