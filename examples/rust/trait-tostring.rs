#![allow(unused_variables)]
#![allow(dead_code)]

//x description="conversion to string"

//x step={
impl std::string::ToString for Circle {
    fn to_string(&self) -> String {
        format!("circle of radius {}", self.radius)
    }
}
//x }


//x pre={
struct Circle {
    radius: i32,
}

fn main() {
    let a = Circle{ radius: 6};    
    println!("{}", a.to_string());
}
//x }

//x explanation="implements the std::string::ToString trait (similar to an interface) for Circle"
