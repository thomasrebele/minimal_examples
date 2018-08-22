
#![allow(unused_variables)]


//x description="add documentation to a public function"
//x pre={
// increment argument by 1
//x }

//x step={
/// increment argument by 1
//x }
//x post={
fn inc(v : u32) -> u32 {
    v + 1
}
//x }
    
fn main() {
    inc(1);
}
