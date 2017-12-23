#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]


fn main() {

//x description="ownership (3)"

//x pre={
let s1 = String::from("abc");
let s2 = s1;

// s1? s2?
//x }

//x step={
// s1 is unavailable, s2 is String "abc"
//x }

//x explanation="String does not implement the Copy trait, so the ownership is moved in assigments"

}
