#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="init struct with fields"

//x pre={
struct Point {
    x: f32,
    y: f32,
}

let x = 1.0;
let y = 2.0;

// task: simplify following expression
let p = Point{x:x, y:y};
//x }

//x step={
let p = Point{x, y};
//x }

}
