#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]


fn main() {

//x description="ownership and functions (1)"

//x pre={
fn f(arg: String) {
}

let s1 = String::from("abc");
f(s1);

// s1?
//x }

//x step={
// s1 is unavailable
//x }

}
