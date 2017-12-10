#![allow(unused_variables)]

fn main() {

//x description="write to file"

//x pre={
// overwrites if exists
let mut file = std::fs::File::create("/tmp/file.txt").unwrap();
//x }

//x step={
// need to import trait
use std::io::Write;

let _ = file.write_all(b"abc");
//x }

}
