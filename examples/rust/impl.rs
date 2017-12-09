
//x description="methods without side effects"
//x level=9

//x pre={
struct Rectangle {
    w: f64,
    h: f64,
}
//x }

//x step={
impl Rectangle {
    fn area(&self) -> f64 {
        self.w * self.h
    }
}
//x }

fn main() {

//x post={
let r = Rectangle{w:10.,h:5.};
r.area();
//x }

}
