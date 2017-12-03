
fn main() {

//x description="tuple variable"
//x step={
    let t = (1, 1.0, false);
    println!("tuple contains ({}, {}, {})", t.0, t.1, t.2);
    // for short tuples (<= 12 elements)
    println!("tuple contains {:?}", t);

    // unwrap
    let (a,b,c) = t;
    println!("tuple contains ({}, {}, {})", a, b, c);
//x }
}
