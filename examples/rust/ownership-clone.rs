#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]


fn main() {

//x description="ownership (1)"
//x level=5

//x pre={
let s1 = String::from("abc");
let s2 = s1.clone();

// s1? s2?
//x }

//x step={
// two different instances of String "abc"
//x }

}

