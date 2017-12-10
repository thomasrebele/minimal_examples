#![allow(dead_code)]
#![allow(unused_imports)]

#[derive(Debug)]
enum Event {
    Start,
    Key(i32),
    Click{x:i32, y:i32},
    End,
}

fn main() {

let e2 = Event::Key(1);
//x description="remove redundancy"

//x pre={
// auto generate code for "{:?}"
match e2 {
    Event::Start => println!("start"),
    Event::End => println!("end"),
    Event::Key(s) => println!("key {}", s),
    Event::Click{x, y} => println!("click {} {}", x, y),
}
//x }

//x step={
use Event::{Start, End, Key, Click};
// or
use Event::*;

match e2 {
    Start => println!("start"),
    End => println!("end"),
    Key(s) => println!("key {}", s),
    Click{x, y} => println!("click {} {}", x, y),
}

//x }

}

