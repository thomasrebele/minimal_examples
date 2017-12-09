#![allow(unused_variables)]
#![allow(unused_mut)]

fn main() {

let _ = std::fs::File::create("/tmp/file.txt");

//x description="read content of file into string"
//x level=15

//x pre={
let mut f = std::fs::File::open("/tmp/file.txt").unwrap();
//x }

//x step={
let mut s = String::new();

// to import trait
use std::io::Read;

let _ = f.read_to_string(&mut s);
//x }
}
