#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() { 

//x description="reference count"

//x pre={
let v = String::from("alice");

// wrap v in reference counted pointer
//x }

//x step={
use std::rc::Rc;
let a = Rc::new(v);
//x }

//x post={
let mut b = a.clone();

assert_eq!(a, b);
assert_eq!(*a, "alice");

// b.push_str("bob"); // compile error "cannot borrow immutable borrowed content as mutable"
//x }

}
