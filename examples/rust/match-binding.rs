
fn main() {

let n = 10;

//x description="value of match case"
//x level=9

/*

//x pre={
match n {
1 ... 12 => println!("which one?"),
_ => (),
}
//x }

*/

//x step={
match n {
n @ 1 ... 12 => println!("which one? {}", n),
_ => (),
};
//x }

}

