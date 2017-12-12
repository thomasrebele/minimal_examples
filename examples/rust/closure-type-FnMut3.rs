#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (6)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || std::mem::drop(x);

fn exec<F>(mut f: F)
where F: FnMut() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// no, closure implements FnOnce trait, which is more restrictive than FnMut trait
//x }

}

