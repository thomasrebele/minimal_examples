#[allow(unused_variables)]
#[allow(dead_code)]

//x description="function return type"
//x level=3

fn pre() {
//x pre={
fn is_even(n: i32) {
// result is n % 2 == 0
}
//x }
}

//x step={
fn is_even(n: i32) -> bool {
    n % 2 == 0
}
//x }
//x explanation="function return value of last statement without semicolon"

//x post={
fn main() {
    println!("is 5 even? {}", is_even(5));
}
//x }

