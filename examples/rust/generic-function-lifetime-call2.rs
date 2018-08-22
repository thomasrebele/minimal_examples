#![allow(dead_code)]
#![allow(unused_variables)]

//x description="calling generic functions with lifetime bounds (2)"

//x pre={
fn max<'a>(x: &'a i32, y: &'a i32) -> &'a i32 {
    if x > y {x} else {y}
}
//x }

//x explanation=""


fn main() {
/*
//x pre={
let x;
let a = 1;
let b = 2;
x = max(&a,&b);
println!("{}", x);

// does this compile ?
//x }
*/
}

/*
//x step={
no; x is declared before a and b,

that means lifetime of reference variable x 
is NOT contained within lifetime of a and b
//x }
*/

