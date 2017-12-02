
//x description="variable of type enum"
//
//x pre={

// auto generate code for "{:?}"
#[derive(Debug)]

enum Event {
    Start,
    Key(i32),
    Click{x:i32, y:i32},
    End,
}
//x }

fn main() {
//x code={
let e1 = Event::Start;
let e2 = Event::Key(1);
let e3 = Event::Click{x:20, y:80};
let e4 = Event::End;

println!("1. {:?}", e1);
// ...
//x }

println!("2. {:?}", e2);
println!("3. {:?}", e3);
println!("4. {:?}", e4);
}
