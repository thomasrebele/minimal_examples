#![allow(dead_code)]

fn main() {

//x description="match for enum"
//x pre={
// auto generate code for "{:?}"
#[derive(Debug)]
enum Event {
    Start,
    Key(i32),
    Click{x:i32, y:i32},
    End,
}

let e2 = Event::Key(1);
//x }

//x code={
match e2 {
    Event::Start => println!("start"),
    Event::End => println!("end"),
    Event::Key(s) => println!("key {}", s),
    Event::Click{x, y} => println!("click {} {}", x, y),
}

//x }

}

