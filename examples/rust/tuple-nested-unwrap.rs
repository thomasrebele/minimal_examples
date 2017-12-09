
fn main() {

//x description="unwrap nested tuple"
//x level=6

//x pre={
let t = ( (1,2), (3,4));
//x }

//x step={
let ((a,b),(c,d)) = t;
//x }

//x post={
println!("tuple contains (({}, {}), ({}, {}))", 
         a, b, c, d);
//x }
}
