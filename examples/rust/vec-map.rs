#[allow(unused_variables)]
#[allow(unused_mut)]


fn main() {

//x description="apply operation on vec elements"
//x pre={
let a = vec![1,2,3];

// transform to string vector with a.iter()...
//x }

//x step={
let b : Vec<String> = a.iter()
    .map(|i| i.to_string())
    .collect();

// or

let b : Vec<String> = a.iter()
    .map(ToString::to_string)
    .collect();

//x }

}
