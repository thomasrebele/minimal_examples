#![allow(unused_variables)]
#![allow(unreachable_code)]
#![allow(dead_code)]

fn main() {

fn dummy() {

//x description="break outer loop and return value"

//x pre={
let a = loop {
    loop {
        // get out of both loops and set a to 1;
    }
};
//x }

}

//x step={
let a = 'outer: loop {
    loop {
        break 'outer 1;
    }
};
//x }

println!("a: {}", a);


}
