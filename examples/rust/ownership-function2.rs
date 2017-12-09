#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]


fn main() {

//x description="ownership and functions (2)"
//x level=9

//x pre={
fn f(arg: String) -> String {
    arg
}

let s1 = String::from("abc");
let s2 = f(s1);

// s1?
//x }

//x step={
println!("{:?}", s2);
// s1 is unavailable, s2 is String "abc"
//x }

}
