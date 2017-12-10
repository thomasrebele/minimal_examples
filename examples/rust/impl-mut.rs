
//x description="methods changing the object state"

//x pre={
struct Counter {
    c: i32,
}
//x }

//x step={
impl Counter {
    fn inc(&mut self) {
        self.c += 1
    }
}
//x }

fn main() {

//x post={
let mut cnt = Counter{c:0};
cnt.inc();
//x }

}
