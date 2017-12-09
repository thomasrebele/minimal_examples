#![allow(dead_code)]

fn main() {

//x description="match for enum (2)"
//x level=4

//x pre={
enum Event {
    Key(i32),
    Click{x:i32, y:i32},
}

let e2 = Event::Key(1);
//x }

//x step={
match e2 {
    Event::Key(s) => println!("key {}", s),
    Event::Click{x, y} => println!("click {} {}", x, y),
}

//x }

}

