#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (2)"

fn main() {

//x pre={
let mut x = Box::new(0);
let closure = || *x += 1;

fn exec<F>(f: F)
where F: Fn() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// no, closure implements FnMut trait, which is more restrictive than Fn trait
//x }

}

