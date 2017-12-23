#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="init struct with fields (2)"

//x pre={
struct Point {
    x: f32,
    y: f32,
    name: String,
}

let p1 = Point {
    name: String::from("p1"),
    x: 1.0, y: 2.0, 
};
// todo: point "p2" with same coordinates as p1
//x }

//x step={
let p = Point {
    name: String::from("p2"), 
    ..p1
};
//x }

}
