#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;

let keys = vec![
    String::from("a"),
    String::from("b")];
let vals = vec![1, 2];

// let map ...
//x }

//x description="collect pairs to hash map"
//x step={
let map : HashMap<_, _> = 
    keys.iter()
        .zip(vals.iter())
        .collect();
//x }

println!("{:?}", map);
}
