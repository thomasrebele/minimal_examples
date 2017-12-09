
#![allow(unused_variables)]

fn main() {

//x description="parse integer from string"
//x level=7
//x pre={
let a = "5";
//x }

//x step={
let b : i32 = a.parse().unwrap();
let c = a.parse::<i32>().unwrap();
//x }
    
}
