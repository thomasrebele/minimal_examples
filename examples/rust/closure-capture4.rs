#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_assignments)]

fn main() {

//x description="closure capturing integer (4)"

//x pre={
let mut a = 10;
{
    let mut f = |x| {a = 20; x+a}; 
    let b = f(1);
}

// a? b?
//x }


//x step={
// a=20, b is unavailable
//x }

}
