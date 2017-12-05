
//x description="if statement"
fn main() {
//x pre={
let n;
// is a number >, =, or < 10? ";
//x }

n = 10;

//x step={
if n > 10 {
    println!("bigger");
} else if n == 10 {
    println!("equals");
} else if n < 10 {
    println!("smaller");
}
//x }
}

//x explanation="{} in if expression are necessary"
