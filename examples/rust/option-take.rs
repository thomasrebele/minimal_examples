
fn main() {

//x description="move value out of option"

//x pre={
let mut a : Option<&str> = Some("alice");
let b;
//x }

//x step={
b = a.take();
//x }

//x post={
assert_eq!(a, None);
assert_eq!(b, Some("alice"));
//x }

}

