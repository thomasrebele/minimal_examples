#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure and borrowing (1)"

//x pre={
// copy type
let a = 1;

let c = || {
    a
};

// a?
//x }

//x step={
// a=1
//x }

}
