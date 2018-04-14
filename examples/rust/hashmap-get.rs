#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;
let mut map : HashMap<String, i32> = HashMap::new();
map.insert(String::from("a"), 1);

let b = map.get("a");
// type of b?
//x }

//x description="hash map"
//x step={
// b is Some(&i32)
//x }

}
