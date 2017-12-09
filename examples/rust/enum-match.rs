#![allow(dead_code)]

fn main() {

//x description="match for enum (1)"
//x level=4

//x pre={
// auto generate code for "{:?}"
#[derive(Debug)]
enum Event {
    Start,
    End,
}

let e1 = Event::Start;
//x }

//x step={
match e1 {
    Event::Start => println!("start"),
    Event::End => println!("end"),
}

//x }

}

