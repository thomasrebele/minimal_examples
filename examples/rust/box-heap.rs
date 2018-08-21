#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="move value from stack to heap"
//x pre={
let a = (0,1);
//x }

//x step={
let a = Box::new(a);
//x }

}
