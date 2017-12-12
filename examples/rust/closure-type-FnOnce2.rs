#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (8)"

fn main() {

//x pre={
let mut x = Box::new(0);
let closure = || *x += 1;

fn exec<F>(f: F)
where F: FnOnce() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// yes, closure implements FnMut trait, which is a subtrait of FnOnce trait
exec(closure);
//x }

}

