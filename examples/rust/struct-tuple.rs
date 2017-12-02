
fn main() {

//x description="struct that behaves like a tuple"

//x code={

// auto generate code for "{:?}"
#[derive(Debug)]
struct Pair(i32, f32);

let pair = Pair(1,0.1);

println!("pair {:?}", pair);

// "decompose"
let Pair(_a, _b) = pair;

//x }

}
