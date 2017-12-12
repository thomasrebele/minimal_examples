#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (5)"

fn main() {

//x pre={
let mut x = Box::new(0);
let closure = || *x += 1;

fn exec<F>(mut f: F)
where F: FnMut() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// yes, closure implements FnMut
exec(closure);
//x }

}

