#![allow(unused_variables)]
#![allow(dead_code)]

//x description="calling static methods"

//x pre={
struct Point {
    x: f64,
    y: f64,
}

impl Point {
    fn origin() -> Point {
        Point{x:0.0, y:0.0}
    }
}
// todo: call method
//x }

fn main() {

//x step={
let p = Point::origin();
//x }

}
