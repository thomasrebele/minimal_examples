
fn main() {

//x description="nested tuple"
//x step={
    let t = ( (1,2), (3,4));
    println!("tuple contains (({}, {}), ({}, {}))", 
             (t.0).0, (t.0).1, (t.1).0, (t.1).1);

    // for short tuples (<= 12 elements)
    println!("tuple contains {:?}", t);

    // unwrap
    let ((a,b),(c,d)) = t;
    println!("tuple contains (({}, {}), ({}, {}))", 
             a, b, c, d);
//x }
}
