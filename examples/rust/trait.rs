#![allow(unused_variables)]
#![allow(dead_code)]

//x description="interfaces"

//x step={
trait Area {
    fn area(&self) -> f32;
}
//x }


//x post={
struct Rectangle {
    w: f32,
    h: f32,
}

impl Area for Rectangle {
    fn area(&self) -> f32 {
        self.w * self.h
    }
}
//x }

fn main() {
    let a = Rectangle{ w: 6., h:7.};
    println!("{}", a.area());
}
