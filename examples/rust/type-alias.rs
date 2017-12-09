
//x description="a type alias for u64"
//x level=5

//x step={
type Second = u64;
type Meter = u64;
//x }

#[allow(unused_variables)]
fn main() {

//x pre={
let seconds = 2 as Second;
let meters = 3 as Meter;
//x }

//x explanation={
// caveat: type aliases still behave like the original type
let c = seconds + meters;
//x }

}
