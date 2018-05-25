#![allow(unused_variables)]
#![allow(unused_mut)]

fn main() {

let _ = std::fs::File::create("/tmp/file.txt");

//x description="open file for reading (match)"

//x pre={
let mut file = std::fs::File::open("/tmp/file.txt");

// let file = match file { ...
//x }

//x step={
let file = match file {
    Ok(f) => f,
    Err(e) => panic!(
        "Error opening file: {}", e),
};
//x }

}
