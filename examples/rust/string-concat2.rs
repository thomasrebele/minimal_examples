#[allow(unused_variables)]
#[allow(unused_assignments)]


fn main() {

//x description="String concatenation"

//x pre={
let s1 = String::from("abc");
let s2 = String::from("def");
let s3 = s1 + &s2;

// s1? s2? s3?
//x }

//x step={
// s1 is unavailable, s2 is "def", s3 is "abcdef"
//x }
}
