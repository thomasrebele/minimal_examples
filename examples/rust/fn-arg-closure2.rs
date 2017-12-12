#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with closure parameter (2)"

fn main() {

fn pre() {
//x pre={
let closure = || println!("hello");

fn twice<F>(f: F)
where F: Fn() -> () {
    f(); f();
}

// todo: rewrite twice without "where"
//x }
}

//x step={
fn twice<F: Fn() -> ()>(f: F) {
    f();
}
//x }

}

