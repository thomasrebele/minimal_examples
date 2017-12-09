
#![allow(unused_variables)]


//x description="unwrap tuple in if statement"
fn main() {
//x pre={
let t = (1,2);
// if ... println!("second component is empty");
// 
//x }

//x step={
if let (a,0) = t {
    println!("second component is empty");
}
//x }

//x explanation="compilation fails for 'if let (a,b) = t', because nothing to test here"
}

