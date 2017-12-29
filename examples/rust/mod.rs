
//x description="modules (1)"

/*
//x pre={
...
    pub fn hello_world() {
        println!("hello world");
    }
}
//x }
*/

//x step={
mod example {
// ...
//x }
    pub fn hello_world() {
        println!("hello world");
    }
}


fn main() {
//x post={
example::hello_world();
//x }
}
