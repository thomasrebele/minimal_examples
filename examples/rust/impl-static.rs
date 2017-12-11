#![allow(unused_variables)]
#![allow(dead_code)]

//x description="declaring static methods"

//x pre={
struct Point {
    x: f64,
    y: f64,
}
//x }

//x step={
impl Point {
    fn origin() -> Point {
        Point{x:0.0, y:0.0}
    }
}
//x }

fn main() {

//x post={
let p = Point::origin();
//x }

}
