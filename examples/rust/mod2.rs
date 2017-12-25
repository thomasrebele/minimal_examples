
//x description="modules (2)"

/*
//x pre={
mod example {
    pub hello_world() {
        println!("hello world");
    }
}
//x }
*/

mod example {
//x step={
// ...
    pub fn hello_world() {
// ...
//x }
        println!("hello world");
    }
}


fn main() {
//x post={
example::hello_world();
//x }
}
