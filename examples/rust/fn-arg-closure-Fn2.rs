#![allow(unused_variables)]
#![allow(dead_code)]

//x description="function with closure parameter; closure restriction (2)"

fn main() {

//x pre={
let x = Box::new(0);
let closure = || println!("{}", x);

// fn ...
// where F: Fn() -> () {
//     f(); f();
// }
//x }

//x step={
fn twice<F>(f: F)
where F: Fn() -> () {
    f(); f();
}
//x }


//x explanation="closure captures x as a reference (&T); it implicitly implements the Fn trait"


//x post={
twice(closure);
//x }

}

