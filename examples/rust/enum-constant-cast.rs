#![allow(dead_code)]

fn main() {

//x description="obtain constant value of blue"
//x level=4

//x pre={
enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff,
}
//x }

//x step={
Color::Blue as i32
//x }
;

}

