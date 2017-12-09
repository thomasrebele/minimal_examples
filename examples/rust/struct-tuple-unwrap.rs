#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="unwrap a tuple-like struct"
//x level=4

//x pre={
struct Pair(i32, f32);

let pair = Pair(1,0.1);
//x }

//x step={
let Pair(a, b) = pair;
//x }

}
