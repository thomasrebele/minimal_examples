#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]

//x description="scope"

fn dummy() {
//x pre={
let mut a = 1;
{
    let mut b = 1;   
    // a? b?

    a = 2; b = 2;
    // a? b?
}
// a? b?
//x }
}


fn main() {

//x step={
let mut a = 1;
{
    let mut b = 1;
    // a=1, b=1

    a = 2; b = 2;
    // a=2, b=2
}
// a=2, b is unavailable
//x }

}
