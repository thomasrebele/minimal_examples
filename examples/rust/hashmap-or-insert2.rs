#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;
let mut map : HashMap<String, i32> = HashMap::new();


// todo: update value for "a"
//x }

//x description="hash map: insert if absent (2)"
//x step={
let a = map.entry(String::from("a")).or_insert(1);
*a += 1;
//x }


}
