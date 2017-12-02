
fn main() {

//x description="struct with fields"

//x code={

// auto generate code for "{:?}"
#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
};

let p = Point{x:1., y:2.};

println!("point {:?}", p);

// "decompose"
let Point{x:_a, y:_b} = p;

//x }

}
