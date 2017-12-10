#[allow(unused_variables)]
#[allow(unused_assignments)]
#[allow(dead_code)]


//x description="variable of type enum Start"

//x pre={
enum Event {
    Start,
    Key(i32),
    Click{x:i32, y:i32},
    End,
}
//x }


#[allow(unused_variables)]

fn main() {
//x step={
let e1 = Event::Start;
//x }
}
