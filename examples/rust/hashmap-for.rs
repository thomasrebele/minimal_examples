#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
use std::collections::HashMap;
let mut map : HashMap<String, i32> = HashMap::new();
map.insert(String::from("a"), 1);
map.insert(String::from("b"), 2);

// for ...
//x }

//x description="hash map and for loop"
//x step={
for (key, val) in &map {
    println!("{}: {}", key, val);
}
//x }


}
