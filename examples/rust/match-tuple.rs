
fn main() {

//x description="match a tuple with unwrapping"
//x level=7

/*

//x pre={
let pair = (1, 2);
match pair {
??? => println!("first = 0"),
??? => println!("second = 0"),
??? => println!("everything else"),
}
//x }

*/

//x step={
let pair = (1, 2);
match pair {
(0,_) => println!("first = 0"),
(_,0) => println!("second = 0"),
_ => println!("everything else"),
}
//x }

}

