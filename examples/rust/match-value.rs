#![allow(unused_variables)]


fn main() {

//x description="value of a match expression"
//x level=4

let boolean = true;

//x pre={
// save value in variable
match boolean {
    false => 0,
    true => 1,
};
//x }

//x step={
let binary = match boolean {
    false => 0,
    true => 1
};
//x }

}
