#![allow(dead_code)]
#![allow(unused_variables)]

//x description="calling generic functions with lifetime bounds (3)"

//x pre={
fn get<'a>(index: &'a usize, v: &'a Vec<i32>) -> &'a i32 {
// ...
//x }
    v.get(*index).unwrap()
}


fn main() {
/*
//x pre={
let v = vec![0,1,2,3];
let r;
{
    let i = 1;
    r = get(&i, &v);
}
println!("{}", r);

// does this compile ?
//x }
*/
}

/*
//x step={
no; `i` does not live long enough
//x }
*/

