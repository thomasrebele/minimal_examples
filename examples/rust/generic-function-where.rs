#![allow(dead_code)]
#![allow(unused_variables)]


//x description="generic function with bounds (2)"

//x pre={
use std::fmt::Debug;

fn top_k<T: Ord + Debug>(t : &[T], k: usize) -> Vec<&T> {
    // ...
    // task: move bounds out of <...>
//x }
    let mut tmp = 
        t.iter()
        .collect::<Vec<_>>();
    tmp.sort();
    tmp.iter()
        .rev()
        .take(k)
        .map(|x| *x)
        .collect::<Vec<_>>()
}

mod dummy {
use std::fmt::Debug;

//x step={
fn top_k<T>(t : &[T], k: usize) -> Vec<&T>
    where T: Ord + Debug {
    // ...
//x }
    Vec::new()
}
}



fn main() {
//x post={
    println!("{:?}", top_k(&[2,1,3,5,4,0], 2));
//x }
}

