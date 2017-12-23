
fn main() {

//x description="option match"

//x pre={
let a : Option<i32>;
//x }

a = Some(1);

//x step={
match a {
    None => println!("none"),
    Some(x) => println!("{}", x)
}
//x }

}

