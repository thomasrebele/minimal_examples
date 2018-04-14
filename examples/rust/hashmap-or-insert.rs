#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;
let mut map : HashMap<String, i32> = HashMap::new();

// todo: insert if absent
//x }

//x description="hash map: insert if absent"
//x step={
map.entry(String::from("a")).or_insert(1);
//x }


}
