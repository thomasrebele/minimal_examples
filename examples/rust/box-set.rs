#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="change content of box"
//x pre={
let mut a : Box<i32> = Box::new(0);
//x }

//x step={
*a = 123;
//x }

//x post={
// a contains 123
//x }

}
