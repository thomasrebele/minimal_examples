#![allow(dead_code)]
#![allow(non_camel_case_types)]


//x description="generic struct with two type parameters"
//x level=8

//x pre={
struct Entry_i32_f64 {
    k: i32, v: f64
}
//x }


//x step={
struct Entry<K, V> {
    k: K, v: V
}
//x }


fn main() {

}

