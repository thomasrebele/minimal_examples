#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]

fn pre() {

//x pre={
fn f(arg: &String) {
// todo: arg.push_str("xyz");
}

let s1 = String::from("abc");
f(&s1);
//x }

}


fn main() {

//x description="ownership and functions (4)"

//x step={
// mut here,
fn f(arg: &mut String) {
    arg.push_str("xyz");
}

// here,
let mut s1 = String::from("abc");
// and here!
f(&mut s1);
//x }

}
