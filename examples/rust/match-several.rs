
fn main() {

let n = 10;

//x description="several match cases combined"

/*

//x pre={
match n {
	??? => println!("one"),
	??? => println!("2, 4, or 6"),
	??? => println!("everything else"),
}
//x }

*/

//x step={
match n {
	1 => println!("one"),
	2|4|6 => println!("2, 4, or 6"),
	_ => println!("everything else"),
}
//x }

}

