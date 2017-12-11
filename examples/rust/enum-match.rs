#![allow(dead_code)]

fn main() {

//x description="match for enum (1)"

// auto generate code for "{:?}"
#[derive(Debug)]
//x pre={
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

