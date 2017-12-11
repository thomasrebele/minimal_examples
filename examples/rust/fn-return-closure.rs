#[allow(unused_variables)]
#[allow(dead_code)]

//x description="function return type"

fn main() {

//x pre={
let inc = |x| x+1;
inc(1);

// todo: return inc with
// fn make_closure(...)
//x }

//x step={
fn make_closure() -> Box<Fn(i32) -> i32> {
    Box::new(|x| x+1)
}
//x }

//x explanation="return type need to have a know size; closures do not have a known size"

}

