#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]


fn main() {

//x description="ownership (2)"

//x pre={
let s1 = 5;
let s2 = s1;

// s1? s2?
//x }

//x step={
// s1=5, s2=5
//x }

//x explanation="i32 implements the Copy trait, so its value is copied in assignments"

}
