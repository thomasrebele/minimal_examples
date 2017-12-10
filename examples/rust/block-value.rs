#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]

fn main() {

//x description="value of expressions"

//x pre={
let a = 0;
let b = {
    a + 1
};
let c = {
    a + 2;
};
let d = {
    let x = a + 3;
    x
};
// a? b? c? d?
//x }

//x step={
// a=0, b=1, c=(), d=3
//x }

}
