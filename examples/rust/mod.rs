
//x description="modules (1)"

//x step={
mod example {
//x }
//x post={
// ...
    pub fn hello_world() {
        println!("hello world");
    }
}
//x }


fn main() {
//x post={
example::hello_world();
//x }
}
