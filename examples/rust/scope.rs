#![allow(dead_code)]
#![allow(unused_variables)]

fn dummy() {
//x pre={
let a = 1;
{
    let b = 1;   
    // a? b?
}
// a? b?
//}
}


fn main() {

//x description="scope"

//x code={
let a = 1;
{
    let b = 1;
    // a: 1, b:1
}
// a:1, b: undefined
//}

}
