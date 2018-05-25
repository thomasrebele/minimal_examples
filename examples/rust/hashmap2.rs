#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x pre={
//use ...
//x }

//x description="hash map (import)"
//x step={
use std::collections::HashMap;
//x }

//x post={
let mut map : HashMap<String, i32> = HashMap::new();

map.insert(String::from("a"), 1);
let a : &i32 = map.get(&String::from("a")).unwrap();
//x }

println!("{}", a);
}
