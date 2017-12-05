
//x description="inline if expression with statements"
fn main() {
//x pre={
let n = 1;
// print sth for every case
println!("is n big or small? {}", 
    if n > 10 {"big"} 
    else {"small"});
//x }

//x step={
println!("is n big or small? {}", 
    if n > 10 {println!("A"); "big"} 
    else {println!("B"); "small"});
//x }
}

//x explanation="{} in if expression are necessary"
