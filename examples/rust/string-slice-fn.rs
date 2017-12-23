#[allow(unused_variables)]
#[allow(unused_assignments)]


fn main() {

//x description="string slice function (1)"

//x pre={
let s = String::from("hello world");
let hello = &s[0..5];
//x }

//x step={
fn print(slice : &str) {
    println!("'{}'", slice);
}
//x }

//x post={
print(hello);
//x }
}
