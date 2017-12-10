
fn main() {

//x description="print a tuple"

//x pre={
let t = (1, 1.0, false);
//x }

//x step={
println!("tuple contains ({}, {}, {})", t.0, t.1, t.2);

// for short tuples (<= 12 elements)
println!("tuple contains {:?}", t);
//x }

}
