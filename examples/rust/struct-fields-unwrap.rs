#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="unwrap a struct with fields"

//x pre={
struct Point {
    x: f32,
    y: f32,
};

let p = Point{x:1., y:2.};
//x }

//x step={
let Point{x:_a, y:_b} = p;
//x }

}
