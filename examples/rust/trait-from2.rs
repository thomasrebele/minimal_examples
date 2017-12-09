#![allow(unused_variables)]
#![allow(dead_code)]

//x description="conversion with From trait (2)"
//x level=11

//x pre={
struct Number {
    value: i32,
}

fn main() {
    let a = Number::from(30);    
    let b : Number = 30.into();
}
//x }

/*
//x pre={
impl std::convert::From<i32> for Number {
//... {
        Number { value: item }
    }
}
//x }
*/

impl std::convert::From<i32> for Number {
//x step={
    fn from(item: i32) -> Self {
//x }
        Number { value: item }
    }
}



//x explanation="implements the std::convert::From trait (similar to an interface) for Number"
