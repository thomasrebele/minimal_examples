#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="get element from vector (1)"
//x pre={
let a = vec![0,1,2,3];
//x }

//x step={
let b = &a[2]; // b : &i32
let c = a.get(2); // c : Option<&i32>
//x }

}
