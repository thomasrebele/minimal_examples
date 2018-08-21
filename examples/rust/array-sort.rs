#[allow(unused_variables)]


fn main() {

//x description="sort array"

//x pre={
let mut a = [2,4,1,3,0];
//x }

//x step={
a.sort();
//x }

//x post={
assert_eq!(a, [0,1,2,3,4]);
//x }

}
