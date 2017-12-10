
fn main() {
//x description="size of datatype"

//x pre={
let x = 1u16;
//x }

println!("size of x in bytes: {}",
//x step={
std::mem::size_of_val(&x)
// returns 2
//x }
);
}
