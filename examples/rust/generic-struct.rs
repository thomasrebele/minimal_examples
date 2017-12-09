#![allow(dead_code)]
#![allow(non_camel_case_types)]


//x description="generic struct"
//x pre={
struct Point_i32 {
    x: i32, y: i32
}

struct Point_f64 {
    x: f64, y: f64
}
//x }


//x step={
struct Point<T> {
    x: T, y: T
}
//x }


fn main() {

}

