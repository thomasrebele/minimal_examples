#![allow(unused_variables)]

fn main() {

//x description="open file for writing (overwriting existing ones)"

//x step={
let file = std::fs::File::create("/tmp/file.txt");
//x }

println!("{:?}", file);

//x post={
// file is of type Result<File>

// need to import trait
use std::io::Write;

let _ = file.unwrap().write_all(b"abc");
//x }


}
