#![allow(dead_code)]


//x description="generic function"
//x pre={
// return reference to first element
fn first_i32(list: &[i32]) -> &i32 {
    &list[0]
}

fn first_char(list: &[char]) -> &char {
    &list[0]
}
//x }


//x step={
fn first<T>(list: &[T]) -> &T {
    &list[0]
}
//x }


fn main() {
    let a = [1,2,3];

    println!("{:?}", first(&a));

}

