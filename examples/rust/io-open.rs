#![allow(unused_variables)]
#![allow(unused_mut)]

fn main() {

let _ = std::fs::File::create("/tmp/file.txt");

//x description="open file for reading (panic if it does not exist)"
//x level=14

//x step={
let mut f = std::fs::File::open("/tmp/file.txt").unwrap();
//x }

}
