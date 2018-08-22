
#![allow(unused_variables)]


fn main() {

//x description="'ref' keyword"

//x pre={
let x = "bob".to_string();
let ref a = x;
//x }

// define b such that a == b
//x }

//x step={
let b = &x;
//x }

//x post={
assert_eq!(a, b);
//x }
}

//x description="'ref' makes 'a' a reference to 'x'; useful in match expressions"


