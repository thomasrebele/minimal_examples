#![allow(dead_code)]

//x description="methods consuming instances"

//x pre={
struct Key {
    v: i32,
}
//x }

//x step={
impl Key {
    fn destroy(self) {

    }
}
//x }

fn main() {

//x post={
let a = Key{v: 1};
a.destroy();

// now a is unavailable
//x }

//x explanation="self is syntactic sugar for self: Self; only works with 'self', not with other identifiers"

}
