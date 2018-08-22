#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="make enum 'copy' instead of 'move'"

//x step={
#[derive(Clone,Copy)]
//x }
//x post={
#[derive(PartialEq,Debug)]
enum Event {
    Start,
    End,
}

let a = Event::Start;
let b = a; // copy a

assert_eq!(a,b);
//x }

}
