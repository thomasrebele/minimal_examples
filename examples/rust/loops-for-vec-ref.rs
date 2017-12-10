#![allow(dead_code)]
#![allow(unreachable_code)]
#![allow(unused_variables)]
#![allow(while_true)]

fn main() {


//x description="types of vector loop"

//x pre={
let a = vec![1, 2];

for i in a {
    // type of i?
}

for j in &a {
    // type of j?
}
//x }

//x step={
// i is i32
// j is &i32 (reference to integer)
//x }

}
