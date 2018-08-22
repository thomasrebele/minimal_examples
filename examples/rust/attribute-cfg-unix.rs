#[allow(unused_variables)]
#[allow(unused_mut)]





fn main() {

//x description="check if compiled on a Unix-like or a Windows OS"

//x step={
#[cfg(any(unix,windows))]
//x }
//x post={
println!("unix or windows!");
//x }



}
