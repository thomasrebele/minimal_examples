
#![allow(unused_variables)]

//x description="add a documentation test"
//x pre={
/// increment argument by 1
/// the following holds: assert_eq!(inc(1), 2);
//x }

//x step={
/// increment argument by 1
/// 
///     # use crate_name::inc;
///     assert_eq!(inc(1), 2);
///
//x post={
pub fn inc(v : u32) -> u32 {
    v + 1
}
//x }
//x }

fn main() {
    assert_eq!(inc(1), 2);
    println!("unfortunately compilation fails with\n   rustdoc --test doc_test.rs");
}
