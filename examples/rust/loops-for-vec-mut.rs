#![allow(dead_code)]
#![allow(unreachable_code)]
#![allow(while_true)]

fn main() {


//x description="change elements of vector"
//x pre={
let mut a = vec![10, 20, 30];

// add 1 to each element
// for ...
//x }

//x step={
for i in &mut a {
    *i += 1;
}
//x }

}
