
fn main() {

let a = 20;
let b = 11;

//x description="match cases with if condition"

/*

//x pre={
match (a,b) {
    ??? => println!("same"),
    ??? => println!("a divisible by 10"),
    ??? => println!("everything else"),
}
//x }

*/

//x step={
match (a,b) {
    (a,b) if a == b => println!("same"),
    (a,_) if a % 10 == 0 => println!("a divisible by 10"),
    _ => println!("everything else"),
}
//x }

}

