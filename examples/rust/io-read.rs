#![allow(unused_variables)]
#![allow(unused_mut)]

fn main() {

let _ = std::fs::File::create("/tmp/file.txt");

//x description="read content of file into string"

//x pre={
let mut f = std::fs::File::open("/tmp/file.txt").unwrap();

use std::io::Read;
let mut s = String::new();
//x }

//x step={
let _ = f.read_to_string(&mut s);
//x }

}
