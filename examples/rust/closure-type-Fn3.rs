#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (3)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || std::mem::drop(x);

fn exec<F>(f: F)
where F: Fn() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// no, closure implements FnOnce trait, which is more restrictive than Fn trait
//x }

}

