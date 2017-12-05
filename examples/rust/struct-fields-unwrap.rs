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
// store in x and y
let Point{x, y} = p;

// store in a and b
let Point{x:a, y:b} = p;

// ignore some values
let Point{x:c, .. } = p;
//x }

}
