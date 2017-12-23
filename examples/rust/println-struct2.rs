#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="print struct"

//x pre={
#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
};

let p = Point{x:1., y:2.};
//x }

//x step={
println!("output: {:#?}", p);
//x }

//x post={
/* output: Point {
    x: 1,
    y: 2
}
*/
//x }

}
