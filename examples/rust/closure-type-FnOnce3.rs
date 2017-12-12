#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (9)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || std::mem::drop(x);

fn exec<F>(f: F)
where F: FnOnce() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// yes, closure implements FnOnce trait
exec(closure);
//x }

}

