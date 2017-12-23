#[allow(unused_variables)]
#[allow(unused_assignments)]


fn main() {

//x description="string slice (2)"

//x pre={
let s = String::from("hello world");

// let world = ... (slice of s)
//x }

//x step={
let world = &s[6..s.len()];
// or
let world = &s[6..];
//x }
}
