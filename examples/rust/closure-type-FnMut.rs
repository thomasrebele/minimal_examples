#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (4)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || println!("{}", x);

fn exec<F>(mut f: F)
where F: FnMut() -> () {
    f();
}

// exec(closure); ?
//x }

//x step={
// yes, closure implements Fn trait, which is a subtrait of FnMut trait
exec(closure);
//x }

}

