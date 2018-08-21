#[allow(unused_variables)]
#[allow(dead_code)]

fn main() {

//x description="cloneable struct"

//x step={
#[derive(Clone)]
//x }
//x post={
struct ID {
    id: i32,
}

let a = ID { id: 1};
let mut b = a.clone(); // make a copy of a
b.id = 2;

assert_eq!(a.id, 1);
assert_eq!(b.id, 2);
//x }

}
