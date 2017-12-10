#![allow(unused_variables)]

fn main() {

//x description="open file for writing (overwriting existing ones)"

//x step={
let f = std::fs::File::create("/tmp/file.txt");

// f is of type Result<File>
//x }

println!("{:?}", f);

}
