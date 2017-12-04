#[allow(unused_variables)]
#[allow(unused_assignments)]
#[allow(dead_code)]


//x description="variable of type enum Click"
//
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
let e3 = Event::Click{x:20, y:80};
//x }
}
