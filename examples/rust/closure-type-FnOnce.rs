#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (7)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || println!("{}", x);

fn exec<F>(f: F)
where F: FnOnce() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// yes, closure implements Fn trait, which is a subtrait of FnOnce trait
exec(closure);
//x }

}

