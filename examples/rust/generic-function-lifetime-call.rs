#![allow(dead_code)]
#![allow(unused_variables)]

//x description="calling generic functions with lifetime bounds (1)"

//x pre={
fn max<'a>(x: &'a i32, y: &'a i32) -> &'a i32 {
    if x > y {x} else {y}
}
//x }


//x explanation=""


fn main() {
//x pre={
let a = 1;
let b = 2;
let x;
x = max(&a,&b);
println!("{}", x);

// does this compile ?
//x }
}

/*
//x step={
yes, lifetime of reference variable x is contained within lifetime of a and b
//x }
*/

