#[allow(unused_variables)]
#[allow(unused_mut)]





fn main() {

//x description="check if NOT compiled on Unix-like OS"

//x step={
#[cfg(not(unix))]
//x }
//x post={
println!("NOT unix!");
//x }



}
