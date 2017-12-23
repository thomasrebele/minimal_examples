#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="print struct (2)"

{
//x pre={
struct Point {
    x: f32,
    y: f32,
};

let p = Point{x:1., y:2.};
//x }
}

//x step={
// auto generate code for "{:?}"
// for the following struct
#[derive(Debug)]
struct Point {
// ...
//x }

    x: f32,
    y: f32,
};

let p = Point{x:1., y:2.};


//x post={
println!("struct {:?}", p);
//x }

}
