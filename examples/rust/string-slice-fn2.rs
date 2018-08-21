#[allow(unused_variables)]
#[allow(unused_assignments)]


fn main() {

//x description="string slice function (2)"

//x pre={
let s = String::from("hello world");

fn print(slice : &str) {
    println!("'{}'", slice);
}

// print s with previous function
//x }

//x step={
print(&s);
//x }
}
