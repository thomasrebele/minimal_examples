#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="get element from vector (2)"
//x level=10
//x pre={
let a = vec![0,1,2,3];

let b = &a[2]; // b : type?
let c = a.get(2); // c : type?
//x }

//x step={
let b = &a[2]; // b : &i32
let c = a.get(2); // c : Option<&i32>
//x }

}
