#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with closure parameter; closure restriction (4)"

fn main() {

//x pre={
let mut x = Box::new(0);
let closure = || *x += 1;

// fn ...
// where F: FnMut() -> () {
//     f(); f();
// }
//x }

//x step={
fn twice<F>(mut f: F)
where F: FnMut() -> () {
    f(); f();
}
//x }


//x explanation="closure captures x as a mutable reference (&mut T); it implicitly implements FnMut trait"


//x post={
twice(closure);
//x }

}

