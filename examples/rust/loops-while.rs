#![allow(dead_code)]
#![allow(unreachable_code)]
#![allow(while_true)]

fn main() {


//x description="loop until condition is fulfilled"
//x pre={
let n = 64;
let mut a = 1;
let mut c = 0;
// log 2 of n?
//x }

//x step={
while a < n {
    a *= 2;
    c += 1;
};

//x }

//x explanation="while does not support returning value with break"

println!("log {}", c);

}
