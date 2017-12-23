#![allow(unused_variables)]
#![allow(unused_mut)]

fn main() {

let _ = std::fs::File::create("/tmp/file.txt");

//x description="read content of file into string (2)"

//x pre={
let mut f = std::fs::File::open("/tmp/file.txt").unwrap();
//x }

//x step={
// to import trait
use std::io::Read;
//x }

//x post={
let mut s = String::new();
let _ = f.read_to_string(&mut s);
//x }
}
