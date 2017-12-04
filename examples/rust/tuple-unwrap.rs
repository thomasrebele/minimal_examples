
fn main() {

//x description="unwrap tuple"
//x pre={
let t = (1, 1.0, false);
//x }

//x step={
let (a,b,c) = t;
//x }

//x post={
println!("tuple contains ({}, {}, {})", a, b, c);
//x }
}
