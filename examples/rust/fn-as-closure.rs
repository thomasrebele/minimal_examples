#[allow(unused_variables)]
#[allow(dead_code)]

//x description="function as closure"

fn main() {
//x pre={
fn function() {
    println!("1");
}

let closure = || println!("2");

fn call<F: Fn()>(f: F) {
    f();
}

// call(function); ?
// call(closure); ?
//x }

//x step={
// both possible
call(function);
call(closure);
//x }

}
