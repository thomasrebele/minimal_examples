#[allow(unused_variables)]


fn main() {

//x description="variable shadowing"

//x pre={
let a : f32 = 1.0;
{
    let a : i32 = 2;
    // a?
}
// a?
//x }

//x step={
let a : f32 = 1.0;
{
    let a : f32 = 2.0;
    // a=2.0
}
// a=1.0
//x }

}
