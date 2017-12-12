#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with closure parameter (6)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || std::mem::drop(x);

// fn ...
// where F: FnOnce() -> () {
//     f(); f();
// }
//x }

//x step={
fn exec<F>(f: F)
where F: FnOnce() -> () {
    f();
}
//x }


//x explanation="closure captures x as value (T); it implicitly implements FnOnce trait"


//x post={
exec(closure);
//x }

}

