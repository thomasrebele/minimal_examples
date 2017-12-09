
//x description="inline if expression"
//x level=3

fn main() {
//x pre={
let n = 1;
// println!("is n big or small? {}", if ...);
//x }

//x step={
println!("is n big or small? {}", 
    if n > 10 {"big"} else {"small"});
//x }
}

//x explanation="{} in if expression are necessary"
