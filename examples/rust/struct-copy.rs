#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="make struct 'copy' instead of 'move'"

//x step={
#[derive(Clone,Copy)]
//x }
//x post={
struct ID {
    id: i32,
}

let a = ID { id: 1};
let mut b = a; // copy a
b.id = 2;

assert_eq!(a.id, 1);
assert_eq!(b.id, 2);
//x }

}
