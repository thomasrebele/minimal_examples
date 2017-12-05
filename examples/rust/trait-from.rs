#![allow(unused_variables)]
#![allow(dead_code)]

//x description="conversion with From trait"

//x step={
impl std::convert::From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}
//x }


//x pre={
struct Number {
    value: i32,
}

fn main() {
    let a = Number::from(30);    
    let b : Number = 30.into();
}
//x }

//x explanation="implements the std::convert::From trait (similar to an interface) for Number"
