#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure and borrowing (4)"

//x pre={
// non-copy type
let a = Box::new(1);

let c = || {
    a
};

c();
// c callable again?
//x }

//x step={
// no, calling 'c' makes 'a' unavailable, so it can only be called once
//x }

}
