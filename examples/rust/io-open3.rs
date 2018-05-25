#![allow(unused_variables)]
#![allow(unused_mut)]

fn main() {

let _ = std::fs::File::create("/tmp/file.txt");

//x description="open file for reading (not found)"

//x pre={
let mut file = std::fs::File::open("/tmp/file.txt");

let file = match file {
    Ok(f) => f,
    
//x }

//x step={
    Err(ref e) 
        if e.kind() == std::io::ErrorKind::NotFound 
//x }

//x post={
        => panic!("file not found"),

    Err(e) => panic!(
        "Error opening file: {}", e),
};
//x }

}
