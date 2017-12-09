
//x description="declare static constant"
//x level=9
//x step={
// global constant
static VERSION: &'static str = "0.1";
//x }

//x pre={
fn main() {
    println!("version {}", VERSION);
}
//x }

//x explanation="'static represents longest possible lifetime, i.e., lifetime of the running program"
