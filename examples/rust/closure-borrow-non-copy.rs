#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure and borrowing (3)"

//x pre={
// non-copy type
let a = Box::new(1);

let c = || {
    a
};

// a?
//x }

//x step={
// a is unavailable
//x }

}
