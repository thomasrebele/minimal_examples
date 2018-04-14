
fn main() {

//x description="reduce values"

//x pre={
let a = vec![0,1,2,3,4,5];

// let sum = a.iter()...
//x }

//x step={
let sum = a.iter().fold(0, |a,b| a+b);
//x }

println!("{}", sum);
}

