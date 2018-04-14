#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;
let mut map : HashMap<String, i32> = HashMap::new();

let k = String::from("a");
let v = 1;
map.insert(k, v);

// k? v?
//x }

//x description="hash map and ownership"
//x step={
// k is unavailable
// v=1, because i32 implements Copy trait
//x }

}
