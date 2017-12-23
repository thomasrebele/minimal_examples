
//x description="modules (2)"

/*
mod example {
    pub fn hello_world() {
        println!("hello world");
    }
}
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
