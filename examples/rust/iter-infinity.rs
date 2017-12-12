
fn main() {

//x description="natural number iterator"

//x step={
let it = 0..;
//x }

//x post={
for i in it {
    println!("{}", i);
    if i==9 {break;}
}
//x }
}

