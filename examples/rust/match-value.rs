#![allow(unused_variables)]


fn main() {

//x description="value of a match expression"

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
