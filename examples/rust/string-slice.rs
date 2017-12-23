#[allow(unused_variables)]
#[allow(unused_assignments)]


fn main() {

//x description="string slice (1)"

//x pre={
let s = String::from("hello world");

// let hello = ... (slice of s)
//x }

//x step={
let hello = &s[0..5];
// or
let hello = &s[..5];
//x }
}
