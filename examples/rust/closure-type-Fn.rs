#![allow(unused_variables)]
#![allow(dead_code)]

//x description="closure restrictions (1)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || println!("{}", x);

fn exec<F>(f: F)
where F: Fn() -> () {
    f();
}

// exec(closure); ?
//x }

exec(closure);
//x step={
// yes, closure implements Fn trait
//x }

}

