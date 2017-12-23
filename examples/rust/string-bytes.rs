#[allow(unused_variables)]
#[allow(unused_assignments)]


fn main() {

//x description="iterate over bytes"

//x pre={
let s = "abc 日本";

// for ...
//x }

//x step={
for b in s.bytes() {
    println!("byte {}", b);
}
//x }

//x explanation="type of b: u8"
}
