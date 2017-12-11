#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure and borrowing (2)"

//x pre={
// non-copy type
let a = 1;

let c = || {
    a
};

c();
// c callable again?
//x }

//x step={
c();
// yes
//x }

// TODO: better explanation

}
