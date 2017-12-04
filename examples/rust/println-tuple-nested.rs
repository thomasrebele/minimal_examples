
fn main() {

//x description="print nested tuple"
//x pre={
let t = ( (1,2), (3,4));
//x }

//x step={
println!("tuple contains (({}, {}), ({}, {}))", 
         (t.0).0, (t.0).1, (t.1).0, (t.1).1);

// for short tuples (<= 12 elements)
println!("tuple contains {:?}", t);
//x }
}
