#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="get element from vector (1)"
//x level=10
//x pre={
let a = vec![0,1,2,3];
//x }

//x step={
let b = &a[2]; 
let c = a.get(2);
//x }


//x explanation="b : &i32, c : Option<&i32>"
}
