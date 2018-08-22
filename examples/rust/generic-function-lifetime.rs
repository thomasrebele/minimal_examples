#![allow(dead_code)]
#![allow(unused_variables)]

//x description="generic function with lifetime bounds"

mod dummy {
//x pre={
fn get(index: usize, v: Vec<i32>) -> i32 {
// ...
//x }
    v.get(index).unwrap().clone()
}
}

//x step={
fn get<'a, 'b>(index: &'a usize, v: &'b Vec<i32>) -> &'b i32 {
// ...
//x }
    v.get(*index).unwrap()
}


fn main() {
//x post={

let v = vec![0,1,2,3];
let r;
{
    let i = 1;
    r = get(&i, &v);
}
println!("{}", r);
//x }
}


