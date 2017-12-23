
//x description="modules (1)"

/*
...
    pub fn hello_world() {
        println!("hello world");
    }
}
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
