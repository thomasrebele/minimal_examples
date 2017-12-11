#[allow(unused_variables)]
#[allow(dead_code)]

//x description="simple macro"

//x step={
macro_rules! say_hello {
    () => (println!("hello");)
}
//x }

//x explanation="the arguments of the macro call are matched with one of the exrpessions before '=>'"

fn main() {
//x post={
say_hello!()
//x }
}
