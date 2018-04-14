#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;
//x }

//x description="hash map"
//x step={
let mut map : HashMap<String, i32> = HashMap::new();
//x }

//x post={
map.insert(String::from("a"), 1);
map.insert(String::from("b"), 2);
//x }

}
