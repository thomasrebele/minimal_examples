
fn main() {

//x description="get n elements from iterator"

//x pre={
let it = 0..;
let n = 5;
//x }

//x step={
let el = it.take(n);
//x }

//x post={
for i in el {
    println!("{}", i);
}
//x }
}

