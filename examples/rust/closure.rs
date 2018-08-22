#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {

//x description="closure"

//x pre={
fn  inc_v1   (x: i32) -> i32 {x+1};
// task: write function as closure
// (with and without type annotation)
//x }

//x step={
let inc_v2 = |x: i32| -> i32 {x+1};
let inc_v3 = |x|             {x+1}; 
let inc_v4 = |x|              x+1 ; 
//x }


//x post={
println!("{}", inc_v3(0_i32));
println!("{}", inc_v4(0_i32));
//x }

//x explanation="omitting types only works if used later"
}
